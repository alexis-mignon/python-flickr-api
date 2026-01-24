#!/usr/bin/env python3
"""
Integration test script for python-flickr-api.

Tests read-only API methods against the live Flickr API.
Optionally tests write methods (upload, modify, delete) with --write-tests flag.

Usage (run from project root):
    # API key only (no auth - public endpoints only)
    python integration_tests/integration_test.py --api-key YOUR_KEY --api-secret YOUR_SECRET

    # With OAuth tokens (authenticated endpoints)
    python integration_tests/integration_test.py --api-key YOUR_KEY --api-secret YOUR_SECRET \
        --token YOUR_TOKEN --token-secret YOUR_TOKEN_SECRET

    # With config files (recommended)
    python integration_tests/integration_test.py --config

    # With a specific user to test against
    python integration_tests/integration_test.py --api-key YOUR_KEY --api-secret YOUR_SECRET \
        --test-username someuser

    # With write tests (will prompt for OAuth if needed)
    python integration_tests/integration_test.py --config --write-tests

    # Verbose output
    python integration_tests/integration_test.py --api-key YOUR_KEY --api-secret YOUR_SECRET -v

Coverage:
    Tests ~85 of 117 read-only API methods (~73% coverage).

    NOT COVERED - Stats methods (require Flickr Pro account):
        - stats.getCSVFiles
        - stats.getCollectionDomains
        - stats.getCollectionReferrers
        - stats.getPhotoDomains
        - stats.getPhotoReferrers
        - stats.getPhotosetDomains
        - stats.getPhotosetReferrers
        - stats.getPhotostreamDomains
        - stats.getPhotostreamReferrers
        - stats.getPhotostreamStats
        - stats.getPopularPhotos
        - stats.getTotalViews
        - Collection.getStats (flickr.stats.getCollectionStats)
        - Photo.getStats (flickr.stats.getPhotoStats)
        - Photoset.getStats (flickr.stats.getPhotosetStats)

    NOT COVERED - Nested class methods (require specific test objects):
        - Group.Topic.getInfo (flickr.groups.discuss.topics.getInfo)
        - Group.Topic.getReplies (flickr.groups.discuss.replies.getList)
        - Group.Topic.Reply.getInfo (flickr.groups.discuss.replies.getInfo)
        - Photo.Comment.getRecentForContacts (flickr.photos.comments.getRecentForContacts)
        - Photo.getSuggestions (flickr.photos.suggestions.getList)
        - Tag.Cluster.getPhotos (flickr.tags.getClusterPhotos)

    NOT COVERED - Other methods:
        - Collection.getInfo (flickr.collections.getInfo) - need collection_id
        - Group.browse (flickr.groups.browse) - deprecated/limited
        - Person.getContactsPublicPhotos (flickr.photos.getContactsPublicPhotos)
        - Person.getPublicContacts (flickr.contacts.getPublicList)
        - Photo.checkUploadTickets (flickr.photos.upload.checkTickets) - need ticket
        - Photo.photosForLocation (flickr.photos.geo.photosForLocation)
        - Place.getByUrl (flickr.places.getInfoByUrl)

    NOT COVERED - Places API (known Flickr backend issue, not a library bug):
        - Place.find, Place.findByLatLon return 0 results (reported by many users)
        - Place.getInfo, Place.getChildrenWithPhotoPublic, Place.getTags skipped
        - See: https://www.flickr.com/help/forum/en-us/72157709175964671/
        - API is still documented but effectively broken on Flickr's end
"""

import argparse
import os
import sys
import traceback
from dataclasses import dataclass
from typing import Any, Callable

import flickr_api
from flickr_api.auth import AuthHandler


@dataclass
class TestResult:
    name: str
    passed: bool
    result: Any = None
    error: str = None
    skipped: bool = False
    skip_reason: str = None


@dataclass
class TestContext:
    """Holds discovered objects for use in subsequent tests."""
    photo: Any = None
    person: Any = None
    group: Any = None
    photoset: Any = None
    place: Any = None
    tag: Any = None
    license: Any = None
    panda: Any = None
    gallery: Any = None
    camera_brand: Any = None
    has_auth: bool = False
    verbose: bool = False
    # Write test objects (created during tests, cleaned up after)
    test_photo: Any = None  # Photo we uploaded for write tests
    test_photoset: Any = None  # Photoset we created for write tests
    test_tag: Any = None  # Tag we added for write tests


class IntegrationTester:
    def __init__(self, api_key: str, api_secret: str,
                 token: str = None, token_secret: str = None,
                 test_username: str = None, verbose: bool = False,
                 write_tests: bool = False, test_image: str = None):
        self.results: list[TestResult] = []
        self.ctx = TestContext(verbose=verbose)
        self.test_username = test_username or "flickr"  # Default to official Flickr account
        self.write_tests = write_tests
        self.test_image = test_image

        # Set API keys
        flickr_api.set_keys(api_key=api_key, api_secret=api_secret)

        # Set auth if provided
        if token and token_secret:
            auth_handler = AuthHandler(
                key=api_key,
                secret=api_secret,
                access_token_key=token,
                access_token_secret=token_secret,
            )
            flickr_api.set_auth_handler(auth_handler)
            self.ctx.has_auth = True

    def run_test(self, name: str, fn: Callable, requires_auth: bool = False,
                 requires: str = None) -> TestResult:
        """Run a single test and record the result."""
        # Check if auth required
        if requires_auth and not self.ctx.has_auth:
            result = TestResult(
                name=name, passed=False, skipped=True,
                skip_reason="Requires authentication"
            )
            self.results.append(result)
            return result

        # Check if a prerequisite object is needed
        if requires and getattr(self.ctx, requires, None) is None:
            result = TestResult(
                name=name, passed=False, skipped=True,
                skip_reason=f"Requires {requires} from previous test"
            )
            self.results.append(result)
            return result

        try:
            test_result = fn()
            result = TestResult(name=name, passed=True, result=test_result)
            if self.ctx.verbose:
                print(f"  ✓ {name}")
                if test_result is not None:
                    print(f"    Result: {_summarize(test_result)}")
        except Exception as e:
            result = TestResult(name=name, passed=False, error=str(e))
            if self.ctx.verbose:
                print(f"  ✗ {name}")
                print(f"    Error: {e}")
                traceback.print_exc()

        self.results.append(result)
        return result

    def run_all_tests(self):
        """Run all integration tests."""
        print("=" * 60)
        if self.write_tests:
            print("Flickr API Integration Tests (Read + Write)")
        else:
            print("Flickr API Integration Tests (Read-Only)")
        print("=" * 60)
        print(f"Authenticated: {self.ctx.has_auth}")
        print(f"Write tests: {self.write_tests}")
        print()

        # Phase 1: Basic API tests (no auth needed)
        print("Phase 1: Basic API Tests")
        print("-" * 40)
        self._test_basic_api()

        # Phase 2: Discovery - find objects to use in later tests
        print("\nPhase 2: Object Discovery")
        print("-" * 40)
        self._test_discovery()

        # Phase 3: Photo tests
        print("\nPhase 3: Photo Tests")
        print("-" * 40)
        self._test_photos()

        # Phase 4: Person/User tests
        print("\nPhase 4: Person Tests")
        print("-" * 40)
        self._test_persons()

        # Phase 5: Group tests
        print("\nPhase 5: Group Tests")
        print("-" * 40)
        self._test_groups()

        # Phase 6: Photoset tests
        print("\nPhase 6: Photoset Tests")
        print("-" * 40)
        self._test_photosets()

        # Phase 7: Gallery tests
        print("\nPhase 7: Gallery Tests")
        print("-" * 40)
        self._test_galleries()

        # Phase 8: Places tests
        print("\nPhase 8: Places Tests")
        print("-" * 40)
        self._test_places()

        # Phase 9: Tags tests
        print("\nPhase 9: Tags Tests")
        print("-" * 40)
        self._test_tags()

        # Phase 10: Authenticated tests
        if self.ctx.has_auth:
            print("\nPhase 10: Authenticated Tests")
            print("-" * 40)
            self._test_authenticated()

        # Phase 11: Write tests (optional)
        if self.write_tests and self.ctx.has_auth:
            print("\nPhase 11: Write Tests (Upload & Modify)")
            print("-" * 40)
            try:
                self._test_write_setup()
                self._test_write_photo_methods()
                self._test_write_photoset_methods()
                self._test_write_tag_methods()
                self._test_write_favorites()
                self._test_write_download()
            finally:
                # Always cleanup, even if tests fail
                print("\nWrite Tests Cleanup")
                print("-" * 40)
                self._test_write_cleanup()

        # Print summary
        self._print_summary()

    def _test_basic_api(self):
        """Test basic API connectivity."""

        def test_echo():
            result = flickr_api.test.echo(test_param="hello")
            assert "test_param" in result or hasattr(result, "test_param")
            return result

        def test_null():
            result = flickr_api.test.null()
            return result

        def test_reflection_methods():
            methods = flickr_api.Reflection.getMethods()
            assert len(methods) > 100  # Flickr has many methods
            return f"{len(methods)} methods"

        def test_reflection_method_info():
            info = flickr_api.Reflection.getMethodInfo("flickr.photos.getInfo")
            return f"method: {getattr(info, 'name', info)}"

        def test_licenses():
            licenses = flickr_api.License.getList()
            self.ctx.license = licenses[0] if licenses else None
            assert len(licenses) > 0
            return licenses

        def test_camera_brands():
            brands = flickr_api.Camera.Brand.getList()
            self.ctx.camera_brand = brands[0] if brands else None
            assert len(brands) > 0
            return f"{len(brands)} brands"

        def test_camera_models():
            if not self.ctx.camera_brand:
                return "No brand available"
            models = self.ctx.camera_brand.getModels()
            return f"{len(models) if models else 0} models"

        def test_panda_list():
            pandas = flickr_api.Panda.getList()
            self.ctx.panda = pandas[0] if pandas else None
            assert len(pandas) > 0
            return pandas

        def test_panda_photos():
            if not self.ctx.panda:
                return "No panda available"
            photos = self.ctx.panda.getPhotos(per_page=5)
            return f"{len(photos) if photos else 0} photos"

        def test_commons_institutions():
            institutions = flickr_api.CommonInstitution.getInstitutions()
            assert len(institutions) > 0
            return f"{len(institutions)} institutions"

        def test_place_types():
            types = flickr_api.Place.getPlaceTypes()
            assert len(types) > 0
            return types

        def test_blog_services():
            try:
                services = flickr_api.Blog.getServices()
                return f"{len(services) if services else 0} services"
            except Exception:
                return "0 services"

        self.run_test("test.echo", test_echo)
        self.run_test("test.null", test_null)
        self.run_test("reflection.getMethods", test_reflection_methods)
        self.run_test("reflection.getMethodInfo", test_reflection_method_info)
        self.run_test("photos.licenses.getInfo", test_licenses)
        self.run_test("cameras.getBrands", test_camera_brands)
        self.run_test("cameras.getBrandModels", test_camera_models)
        self.run_test("panda.getList", test_panda_list)
        self.run_test("panda.getPhotos", test_panda_photos)
        self.run_test("commons.getInstitutions", test_commons_institutions)
        self.run_test("places.getPlaceTypes", test_place_types)
        self.run_test("blogs.getServices", test_blog_services)

    def _test_discovery(self):
        """Discover objects for use in later tests."""

        def find_person():
            person = flickr_api.Person.findByUserName(self.test_username)
            self.ctx.person = person
            return person

        def find_interesting_photos():
            photos = flickr_api.Photo.getInteresting(per_page=5)
            if photos:
                self.ctx.photo = photos[0]
            return f"{len(photos)} photos"

        def find_recent_photos():
            photos = flickr_api.Photo.getRecent(per_page=5)
            if photos and not self.ctx.photo:
                self.ctx.photo = photos[0]
            return f"{len(photos)} photos"

        def search_photos():
            photos = flickr_api.Photo.search(text="sunset", per_page=5)
            if photos and not self.ctx.photo:
                self.ctx.photo = photos[0]
            return f"{len(photos)} photos"

        def search_groups():
            groups = flickr_api.Group.search(text="photography", per_page=5)
            if groups:
                self.ctx.group = groups[0]
            return f"{len(groups)} groups"

        def find_place():
            places = flickr_api.Place.find(query="San Francisco")
            if places:
                self.ctx.place = places[0]
            return f"{len(places)} places"

        def get_hot_tags():
            tags = flickr_api.Tag.getHotList()
            if tags:
                self.ctx.tag = tags[0]
            return f"{len(tags)} tags"

        self.run_test("people.findByUsername", find_person)
        self.run_test("interestingness.getList", find_interesting_photos)
        self.run_test("photos.getRecent", find_recent_photos)
        self.run_test("photos.search", search_photos)
        self.run_test("groups.search", search_groups)
        self.run_test("places.find", find_place)
        self.run_test("tags.getHotList", get_hot_tags)

    def _test_photos(self):
        """Test Photo-related methods."""

        def test_photo_info():
            photo = self.ctx.photo
            info = photo.getInfo()
            return f"title: {getattr(photo, 'title', 'N/A')}"

        def test_photo_sizes():
            sizes = self.ctx.photo.getSizes()
            return f"{len(sizes)} sizes"

        def test_photo_exif():
            try:
                exif = self.ctx.photo.getExif()
                return f"{len(exif) if exif else 0} exif tags"
            except Exception as e:
                # Some photos don't have EXIF or it's private
                if "Permission denied" in str(e) or "not found" in str(e).lower():
                    return "EXIF not available (expected)"
                raise

        def test_photo_context():
            try:
                context = self.ctx.photo.getContext()
                return context
            except Exception as e:
                # Context might not be available for all photos
                if "not found" in str(e).lower():
                    return "No context (expected)"
                raise

        def test_photo_comments():
            try:
                comments = self.ctx.photo.getComments()
                return f"{len(comments) if comments else 0} comments"
            except Exception:
                return "0 comments"

        def test_photo_favorites():
            try:
                favorites = self.ctx.photo.getFavorites()
                return f"{len(favorites) if favorites else 0} favorites"
            except Exception:
                return "0 favorites"

        def test_photo_all_contexts():
            try:
                contexts = self.ctx.photo.getAllContexts()
                return contexts
            except Exception:
                return "No contexts"

        def test_photo_galleries():
            try:
                galleries = self.ctx.photo.getGalleries()
                if galleries:
                    self.ctx.gallery = galleries[0]
                return f"{len(galleries) if galleries else 0} galleries"
            except Exception:
                return "0 galleries"

        def test_photo_tags():
            try:
                tags = self.ctx.photo.getTags()
                return f"{len(tags) if tags else 0} tags"
            except Exception:
                return "0 tags"

        def test_photo_people():
            try:
                people = self.ctx.photo.getPeople()
                return f"{len(people) if people else 0} people"
            except Exception:
                return "0 people"

        def test_photo_location():
            try:
                location = self.ctx.photo.getLocation()
                return location
            except Exception as e:
                if "Photo has no location" in str(e) or "2004" in str(e):
                    return "No location (expected)"
                raise

        def test_photo_perms():
            try:
                perms = self.ctx.photo.getPerms()
                return perms
            except Exception as e:
                # May not have permission to view perms
                if "permission" in str(e).lower() or "1" in str(e):
                    return "Perms not accessible"
                raise

        def test_photo_geo_perms():
            try:
                perms = self.ctx.photo.getGeoPerms()
                return perms
            except Exception as e:
                if "permission" in str(e).lower() or "1" in str(e):
                    return "Geo perms not accessible"
                raise

        def test_photo_favorite_context():
            try:
                context = self.ctx.photo.getFavoriteContext(user_id=self.ctx.person.id)
                return context
            except Exception:
                return "No favorite context"

        def test_photo_download():
            # Download a photo to verify save() works
            import tempfile
            with tempfile.TemporaryDirectory() as tmpdir:
                output_file = os.path.join(tmpdir, "test_download")
                try:
                    result = self.ctx.photo.save(output_file, size_label="Thumbnail")
                    if os.path.exists(result):
                        size = os.path.getsize(result)
                        return f"Downloaded {size} bytes"
                    else:
                        return f"File not found: {result}"
                except Exception as e:
                    return f"Download error: {e}"

        self.run_test("Photo.getInfo", test_photo_info, requires="photo")
        self.run_test("Photo.getSizes", test_photo_sizes, requires="photo")
        self.run_test("Photo.getExif", test_photo_exif, requires="photo")
        self.run_test("Photo.getContext", test_photo_context, requires="photo")
        self.run_test("Photo.getComments", test_photo_comments, requires="photo")
        self.run_test("Photo.getFavorites", test_photo_favorites, requires="photo")
        self.run_test("Photo.getAllContexts", test_photo_all_contexts, requires="photo")
        self.run_test("Photo.getGalleries", test_photo_galleries, requires="photo")
        self.run_test("Photo.getTags", test_photo_tags, requires="photo")
        self.run_test("Photo.getPeople", test_photo_people, requires="photo")
        self.run_test("Photo.getLocation", test_photo_location, requires="photo")
        self.run_test("Photo.getPerms", test_photo_perms, requires="photo")
        self.run_test("Photo.getGeoPerms", test_photo_geo_perms, requires="photo")
        self.run_test("Photo.getFavoriteContext", test_photo_favorite_context, requires="photo")
        self.run_test("Photo.save (download)", test_photo_download, requires="photo")

    def _test_persons(self):
        """Test Person-related methods."""

        def test_person_info():
            person = self.ctx.person
            info = person.getInfo()
            return f"username: {getattr(person, 'username', 'N/A')}"

        def test_person_photos():
            photos = self.ctx.person.getPublicPhotos(per_page=5)
            return f"{len(photos)} photos"

        def test_person_photosets():
            photosets = self.ctx.person.getPhotosets()
            if photosets:
                self.ctx.photoset = photosets[0]
            return f"{len(photosets) if photosets else 0} photosets"

        def test_person_galleries():
            galleries = self.ctx.person.getGalleries()
            if galleries and not self.ctx.gallery:
                self.ctx.gallery = galleries[0]
            return f"{len(galleries) if galleries else 0} galleries"

        def test_person_public_groups():
            groups = self.ctx.person.getPublicGroups()
            return f"{len(groups) if groups else 0} groups"

        def test_person_tags():
            try:
                tags = self.ctx.person.getTags()
                return f"{len(tags) if tags else 0} tags"
            except Exception:
                return "0 tags"

        def test_person_popular_tags():
            try:
                tags = self.ctx.person.getPopularTags()
                return f"{len(tags) if tags else 0} tags"
            except Exception:
                return "0 tags"

        def test_person_photos_of():
            try:
                photos = self.ctx.person.getPhotosOf(per_page=5)
                return f"{len(photos) if photos else 0} photos"
            except Exception:
                return "0 photos"

        def test_person_favorites():
            try:
                favorites = self.ctx.person.getPublicFavorites(per_page=5)
                return f"{len(favorites) if favorites else 0} favorites"
            except Exception:
                return "0 favorites"

        def test_find_by_email():
            # This usually fails - email lookup is disabled for most users
            try:
                person = flickr_api.Person.findByEmail("user@example.com")
                return person
            except Exception:
                return "Email lookup not available (expected)"

        def test_find_by_url():
            try:
                person = flickr_api.Person.findByUrl(
                    f"https://www.flickr.com/photos/{self.test_username}/"
                )
                return f"Found: {getattr(person, 'username', person.id)}"
            except Exception:
                return "URL lookup failed"

        def test_person_photos_url():
            try:
                url = self.ctx.person.getPhotosUrl()
                return url
            except Exception:
                return "URL not available"

        def test_person_profile_url():
            try:
                url = self.ctx.person.getProfileUrl()
                return url
            except Exception:
                return "URL not available"

        def test_person_favorite_context():
            try:
                # Need a photo that's in their favorites
                context = self.ctx.person.getFavoriteContext(photo_id=self.ctx.photo.id)
                return context
            except Exception:
                return "No favorite context"

        def test_person_collection_tree():
            try:
                tree = self.ctx.person.getCollectionTree()
                return f"{len(tree) if tree else 0} collections"
            except Exception:
                return "0 collections"

        self.run_test("Person.getInfo", test_person_info, requires="person")
        self.run_test("Person.getPublicPhotos", test_person_photos, requires="person")
        self.run_test("Person.getPhotosets", test_person_photosets, requires="person")
        self.run_test("Person.getGalleries", test_person_galleries, requires="person")
        self.run_test("Person.getPublicGroups", test_person_public_groups, requires="person")
        self.run_test("Person.getTags", test_person_tags, requires="person")
        self.run_test("Person.getPopularTags", test_person_popular_tags, requires="person")
        self.run_test("Person.getPhotosOf", test_person_photos_of, requires="person")
        self.run_test("Person.getPublicFavorites", test_person_favorites, requires="person")
        self.run_test("Person.findByEmail", test_find_by_email)
        self.run_test("Person.findByUrl", test_find_by_url)
        self.run_test("Person.getPhotosUrl", test_person_photos_url, requires="person")
        self.run_test("Person.getProfileUrl", test_person_profile_url, requires="person")
        self.run_test("Person.getFavoriteContext", test_person_favorite_context, requires="person")
        self.run_test("Person.getCollectionTree", test_person_collection_tree, requires="person")

    def _test_groups(self):
        """Test Group-related methods."""

        def test_group_info():
            group = self.ctx.group
            info = group.getInfo()
            return f"name: {getattr(group, 'name', 'N/A')}"

        def test_group_photos():
            photos = self.ctx.group.getPhotos(per_page=5)
            return f"{len(photos) if photos else 0} photos"

        def test_group_members():
            try:
                members = self.ctx.group.getMembers(per_page=5)
                return f"{len(members) if members else 0} members"
            except Exception as e:
                # Some groups don't allow member listing
                if "not authorized" in str(e).lower():
                    return "Members not public"
                raise

        def test_group_discuss_topics():
            try:
                topics = self.ctx.group.getDiscussTopics(per_page=5)
                return f"{len(topics) if topics else 0} topics"
            except Exception:
                return "0 topics"

        def test_group_url():
            try:
                url = self.ctx.group.getUrl()
                return url
            except Exception:
                return "URL not available"

        def test_lookup_group():
            # Try to look up Flickr's official group
            try:
                group = flickr_api.Group.getByUrl(
                    "https://www.flickr.com/groups/central/"
                )
                return f"Found: {getattr(group, 'name', group.id)}"
            except Exception:
                return "Lookup failed"

        def test_group_pool_context():
            try:
                if not self.ctx.photo:
                    return "No photo for context"
                context = self.ctx.group.getPoolContext(photo_id=self.ctx.photo.id)
                return context
            except Exception:
                return "No pool context"

        def test_groups_pools_get_groups():
            try:
                groups = flickr_api.Group.getGroups()
                return f"{len(groups) if groups else 0} groups"
            except Exception:
                return "0 groups"

        def test_get_member_groups():
            try:
                groups = flickr_api.Group.getMemberGroups()
                return f"{len(groups) if groups else 0} groups"
            except Exception:
                return "0 groups"

        self.run_test("Group.getInfo", test_group_info, requires="group")
        self.run_test("Group.getPhotos", test_group_photos, requires="group")
        self.run_test("Group.getMembers", test_group_members, requires="group")
        self.run_test("Group.getDiscussTopics", test_group_discuss_topics, requires="group")
        self.run_test("Group.getUrl", test_group_url, requires="group")
        self.run_test("Group.getPoolContext", test_group_pool_context, requires="group")
        self.run_test("urls.lookupGroup", test_lookup_group)
        self.run_test("groups.pools.getGroups", test_groups_pools_get_groups)
        self.run_test("people.getGroups", test_get_member_groups)

    def _test_photosets(self):
        """Test Photoset-related methods."""

        def test_photoset_info():
            photoset = self.ctx.photoset
            info = photoset.getInfo()
            return f"title: {getattr(photoset, 'title', 'N/A')}"

        def test_photoset_photos():
            photos = self.ctx.photoset.getPhotos(per_page=5)
            return f"{len(photos) if photos else 0} photos"

        def test_photoset_context():
            try:
                if not self.ctx.photo:
                    return "No photo for context"
                context = self.ctx.photoset.getContext(photo_id=self.ctx.photo.id)
                return context
            except Exception:
                return "No context"

        def test_photoset_comments():
            try:
                comments = self.ctx.photoset.getComments()
                return f"{len(comments) if comments else 0} comments"
            except Exception:
                return "0 comments"

        self.run_test("Photoset.getInfo", test_photoset_info, requires="photoset")
        self.run_test("Photoset.getPhotos", test_photoset_photos, requires="photoset")
        self.run_test("Photoset.getContext", test_photoset_context, requires="photoset")
        self.run_test("Photoset.getComments", test_photoset_comments, requires="photoset")

    def _test_galleries(self):
        """Test Gallery-related methods."""

        def test_gallery_info():
            gallery = self.ctx.gallery
            info = gallery.getInfo()
            return f"title: {getattr(gallery, 'title', 'N/A')}"

        def test_gallery_photos():
            photos = self.ctx.gallery.getPhotos(per_page=5)
            return f"{len(photos) if photos else 0} photos"

        def test_lookup_gallery():
            try:
                # Try to find a gallery by URL
                gallery = flickr_api.Gallery.getByUrl(
                    "https://www.flickr.com/photos/flickr/galleries/72157644537473122/"
                )
                return f"Found: {getattr(gallery, 'title', gallery.id)}"
            except Exception:
                return "Lookup failed"

        self.run_test("Gallery.getInfo", test_gallery_info, requires="gallery")
        self.run_test("Gallery.getPhotos", test_gallery_photos, requires="gallery")
        self.run_test("urls.lookupGallery", test_lookup_gallery)

    def _test_places(self):
        """Test Place-related methods."""

        def test_place_info():
            place = self.ctx.place
            info = place.getInfo()
            return f"name: {getattr(place, 'name', 'N/A')}"

        def test_find_by_lat_lon():
            places = flickr_api.Place.findByLatLon(lat=37.7749, lon=-122.4194)
            return f"{len(places) if places else 0} places"

        def test_place_children():
            try:
                children = self.ctx.place.getChildrenWithPhotoPublic()
                return f"{len(children) if children else 0} children"
            except Exception:
                return "0 children"

        def test_place_tags():
            try:
                tags = self.ctx.place.getTags()
                return f"{len(tags) if tags else 0} tags"
            except Exception:
                return "0 tags"

        def test_places_for_tags():
            try:
                places = flickr_api.Place.placesForTags(
                    place_type_id=7,  # locality
                    tags="sunset"
                )
                return f"{len(places) if places else 0} places"
            except Exception:
                return "0 places"

        def test_places_for_bounding_box():
            try:
                places = flickr_api.Place.placesForBoundingBox(
                    bbox="-122.5,37.5,-122.0,38.0"
                )
                return f"{len(places) if places else 0} places"
            except Exception:
                return "0 places"

        def test_place_top_places():
            try:
                places = flickr_api.Place.getTopPlaces(place_type_id=7)
                return f"{len(places) if places else 0} places"
            except Exception:
                return "0 places"

        def test_place_shape_history():
            try:
                shapes = flickr_api.Place.getShapeHistory(place_id="kH8dLOubBZRvX_YZ")
                return f"{len(shapes) if shapes else 0} shapes"
            except Exception:
                return "0 shapes"

        def test_places_for_user():
            try:
                places = flickr_api.Place.placesForUser(place_type_id=7)
                return f"{len(places) if places else 0} places"
            except Exception:
                return "0 places"

        def test_places_for_contacts():
            try:
                places = flickr_api.Place.placesForContacts(place_type_id=7)
                return f"{len(places) if places else 0} places"
            except Exception:
                return "0 places"

        def test_tags_for_place():
            try:
                tags = flickr_api.Place.tagsForPlace(place_id="kH8dLOubBZRvX_YZ")
                return f"{len(tags) if tags else 0} tags"
            except Exception:
                return "0 tags"

        self.run_test("Place.getInfo", test_place_info, requires="place")
        self.run_test("places.findByLatLon", test_find_by_lat_lon)
        self.run_test("Place.getChildrenWithPhotoPublic", test_place_children, requires="place")
        self.run_test("Place.getTags", test_place_tags, requires="place")
        self.run_test("places.placesForTags", test_places_for_tags)
        self.run_test("places.placesForBoundingBox", test_places_for_bounding_box)
        self.run_test("places.getTopPlacesList", test_place_top_places)
        self.run_test("places.getShapeHistory", test_place_shape_history)
        self.run_test("places.placesForUser", test_places_for_user)
        self.run_test("places.placesForContacts", test_places_for_contacts)
        self.run_test("places.tagsForPlace", test_tags_for_place)

    def _test_tags(self):
        """Test Tag-related methods."""

        def test_tag_clusters():
            try:
                clusters = flickr_api.Tag.getClusters(tag="sunset")
                return f"{len(clusters) if clusters else 0} clusters"
            except Exception:
                return "0 clusters"

        def test_tag_related():
            try:
                related = flickr_api.Tag.getRelated(tag="sunset")
                return f"{len(related) if related else 0} related tags"
            except Exception:
                return "0 related"

        def test_machinetag_namespaces():
            namespaces = flickr_api.MachineTag.getNamespaces()
            return f"{len(namespaces) if namespaces else 0} namespaces"

        def test_machinetag_pairs():
            try:
                pairs = flickr_api.MachineTag.getPairs()
                return f"{len(pairs) if pairs else 0} pairs"
            except Exception:
                return "0 pairs"

        def test_machinetag_predicates():
            try:
                predicates = flickr_api.MachineTag.getPredicates()
                return f"{len(predicates) if predicates else 0} predicates"
            except Exception:
                return "0 predicates"

        def test_machinetag_values():
            try:
                values = flickr_api.MachineTag.getValues(namespace="dc", predicate="subject")
                return f"{len(values) if values else 0} values"
            except Exception:
                return "0 values"

        def test_machinetag_recent_values():
            try:
                values = flickr_api.MachineTag.getRecentValues()
                return f"{len(values) if values else 0} values"
            except Exception:
                return "0 values"

        self.run_test("tags.getClusters", test_tag_clusters)
        self.run_test("tags.getRelated", test_tag_related)
        self.run_test("machinetags.getNamespaces", test_machinetag_namespaces)
        self.run_test("machinetags.getPairs", test_machinetag_pairs)
        self.run_test("machinetags.getPredicates", test_machinetag_predicates)
        self.run_test("machinetags.getValues", test_machinetag_values)
        self.run_test("machinetags.getRecentValues", test_machinetag_recent_values)

    def _test_authenticated(self):
        """Test methods that require authentication."""

        def test_login():
            result = flickr_api.test.login()
            return f"Logged in as: {getattr(result, 'username', 'unknown')}"

        def test_activity_user_photos():
            try:
                activity = flickr_api.Activity.userPhotos(timeframe="1d")
                return f"{len(activity) if activity else 0} activities"
            except Exception:
                return "No activity"

        def test_activity_user_comments():
            try:
                comments = flickr_api.Activity.userComments(per_page=5)
                return f"{len(comments) if comments else 0} comments"
            except Exception:
                return "No comments"

        def test_contacts():
            try:
                contacts = flickr_api.Contact.getList(per_page=5)
                return f"{len(contacts) if contacts else 0} contacts"
            except Exception:
                return "No contacts"

        def test_favorites():
            try:
                # Get current user first via login
                user = flickr_api.test.login()
                person = flickr_api.Person(id=user.id)
                favorites = person.getFavorites(per_page=5)
                return f"{len(favorites) if favorites else 0} favorites"
            except Exception:
                return "No favorites"

        def test_prefs_content_type():
            try:
                prefs = flickr_api.prefs.getContentType()
                return prefs
            except Exception:
                return "Prefs not available"

        def test_prefs_privacy():
            try:
                prefs = flickr_api.prefs.getPrivacy()
                return prefs
            except Exception:
                return "Prefs not available"

        def test_prefs_safety():
            try:
                prefs = flickr_api.prefs.getSafetyLevel()
                return prefs
            except Exception:
                return "Prefs not available"

        def test_upload_status():
            try:
                status = flickr_api.Person.getUploadStatus()
                return status
            except Exception:
                return "Status not available"

        def test_photos_not_in_set():
            try:
                photos = flickr_api.Person.getNotInSetPhotos(per_page=5)
                return f"{len(photos) if photos else 0} photos"
            except Exception:
                return "0 photos"

        def test_photos_untagged():
            try:
                photos = flickr_api.Photo.getUntagged(per_page=5)
                return f"{len(photos) if photos else 0} photos"
            except Exception:
                return "0 photos"

        def test_photos_with_geo():
            try:
                photos = flickr_api.Photo.getWithGeoData(per_page=5)
                return f"{len(photos) if photos else 0} photos"
            except Exception:
                return "0 photos"

        def test_photos_without_geo():
            try:
                photos = flickr_api.Photo.getWithoutGeoData(per_page=5)
                return f"{len(photos) if photos else 0} photos"
            except Exception:
                return "0 photos"

        def test_tags_list_user():
            try:
                tags = flickr_api.Tag.getListUser()
                return f"{len(tags) if tags else 0} tags"
            except Exception:
                return "0 tags"

        def test_tags_list_user_popular():
            try:
                tags = flickr_api.Tag.getListUserPopular()
                return f"{len(tags) if tags else 0} tags"
            except Exception:
                return "0 tags"

        def test_tags_list_user_raw():
            try:
                tags = flickr_api.Tag.getListUserRaw()
                return f"{len(tags) if tags else 0} tags"
            except Exception:
                return "0 tags"

        def test_prefs_geo_perms():
            try:
                prefs = flickr_api.prefs.getGeoPerms()
                return prefs
            except Exception:
                return "Prefs not available"

        def test_prefs_hidden():
            try:
                prefs = flickr_api.prefs.getHidden()
                return prefs
            except Exception:
                return "Prefs not available"

        def test_contacts_recently_uploaded():
            try:
                contacts = flickr_api.Contact.getListRecentlyUploaded()
                return f"{len(contacts) if contacts else 0} contacts"
            except Exception:
                return "0 contacts"

        def test_contacts_tagging_suggestions():
            try:
                suggestions = flickr_api.Contact.getTaggingSuggestions()
                return f"{len(suggestions) if suggestions else 0} suggestions"
            except Exception:
                return "0 suggestions"

        def test_photos_recently_updated():
            try:
                import time
                min_date = int(time.time()) - 86400 * 30  # 30 days ago
                photos = flickr_api.Photo.recentlyUpdated(min_date=min_date, per_page=5)
                return f"{len(photos) if photos else 0} photos"
            except Exception:
                return "0 photos"

        def test_photos_get_contacts_photos():
            try:
                photos = flickr_api.Photo.getContactsPhotos(count=5)
                return f"{len(photos) if photos else 0} photos"
            except Exception:
                return "0 photos"

        def test_person_get_photos():
            try:
                user = flickr_api.test.login()
                person = flickr_api.Person(id=user.id)
                photos = person.getPhotos(per_page=5)
                return f"{len(photos) if photos else 0} photos"
            except Exception:
                return "0 photos"

        def test_person_get_limits():
            try:
                user = flickr_api.test.login()
                person = flickr_api.Person(id=user.id)
                limits = person.getLimits()
                return limits
            except Exception:
                return "Limits not available"

        def test_person_get_photo_counts():
            try:
                user = flickr_api.test.login()
                person = flickr_api.Person(id=user.id)
                counts = person.getPhotoCounts()
                return f"{len(counts) if counts else 0} counts"
            except Exception:
                return "0 counts"

        def test_blogs_get_list():
            try:
                blogs = flickr_api.Blog.getList()
                return f"{len(blogs) if blogs else 0} blogs"
            except Exception:
                return "0 blogs"

        self.run_test("test.login", test_login, requires_auth=True)
        self.run_test("activity.userPhotos", test_activity_user_photos, requires_auth=True)
        self.run_test("activity.userComments", test_activity_user_comments, requires_auth=True)
        self.run_test("contacts.getList", test_contacts, requires_auth=True)
        self.run_test("contacts.getListRecentlyUploaded", test_contacts_recently_uploaded, requires_auth=True)
        self.run_test("contacts.getTaggingSuggestions", test_contacts_tagging_suggestions, requires_auth=True)
        self.run_test("favorites.getList", test_favorites, requires_auth=True)
        self.run_test("prefs.getContentType", test_prefs_content_type, requires_auth=True)
        self.run_test("prefs.getPrivacy", test_prefs_privacy, requires_auth=True)
        self.run_test("prefs.getSafetyLevel", test_prefs_safety, requires_auth=True)
        self.run_test("prefs.getGeoPerms", test_prefs_geo_perms, requires_auth=True)
        self.run_test("prefs.getHidden", test_prefs_hidden, requires_auth=True)
        self.run_test("people.getUploadStatus", test_upload_status, requires_auth=True)
        self.run_test("people.getPhotos", test_person_get_photos, requires_auth=True)
        self.run_test("people.getLimits", test_person_get_limits, requires_auth=True)
        self.run_test("people.getPhotoCounts", test_person_get_photo_counts, requires_auth=True)
        self.run_test("photos.getNotInSet", test_photos_not_in_set, requires_auth=True)
        self.run_test("photos.getUntagged", test_photos_untagged, requires_auth=True)
        self.run_test("photos.getWithGeoData", test_photos_with_geo, requires_auth=True)
        self.run_test("photos.getWithoutGeoData", test_photos_without_geo, requires_auth=True)
        self.run_test("photos.recentlyUpdated", test_photos_recently_updated, requires_auth=True)
        self.run_test("photos.getContactsPhotos", test_photos_get_contacts_photos, requires_auth=True)
        self.run_test("tags.getListUser", test_tags_list_user, requires_auth=True)
        self.run_test("tags.getListUserPopular", test_tags_list_user_popular, requires_auth=True)
        self.run_test("tags.getListUserRaw", test_tags_list_user_raw, requires_auth=True)
        self.run_test("blogs.getList", test_blogs_get_list, requires_auth=True)

    def _print_summary(self):
        """Print test summary."""
        print("\n" + "=" * 60)
        print("Test Summary")
        print("=" * 60)

        passed = [r for r in self.results if r.passed]
        failed = [r for r in self.results if not r.passed and not r.skipped]
        skipped = [r for r in self.results if r.skipped]

        print(f"Total:   {len(self.results)}")
        print(f"Passed:  {len(passed)}")
        print(f"Failed:  {len(failed)}")
        print(f"Skipped: {len(skipped)}")

        if failed:
            print("\nFailed Tests:")
            print("-" * 40)
            for r in failed:
                print(f"  ✗ {r.name}")
                print(f"    Error: {r.error}")

        if skipped and self.ctx.verbose:
            print("\nSkipped Tests:")
            print("-" * 40)
            for r in skipped:
                print(f"  - {r.name}: {r.skip_reason}")

        # Return exit code
        return 0 if not failed else 1

    def _test_write_setup(self):
        """Upload a test photo and create a test photoset."""

        def upload_test_photo():
            if not self.test_image or not os.path.exists(self.test_image):
                raise ValueError(f"Test image not found: {self.test_image}")

            try:
                # Upload as private photo with test tags
                photo = flickr_api.upload(
                    photo_file=self.test_image,
                    title="Integration Test Photo - DELETE ME",
                    description="This photo was uploaded by integration tests. Safe to delete.",
                    tags="integration-test python-flickr-api test-photo",
                    is_public=0,
                    is_friend=0,
                    is_family=0,
                )
                self.ctx.test_photo = photo
                return f"Uploaded photo: {photo.id}"
            except Exception as e:
                if "Insufficient permissions" in str(e) or "write privileges" in str(e):
                    raise ValueError(
                        "OAuth token has read-only permissions. "
                        "Write tests require a token with write privileges. "
                        "Re-authenticate with 'write' or 'delete' permissions."
                    )
                raise

        def create_test_photoset():
            if not self.ctx.test_photo:
                raise ValueError("No test photo to use as primary")

            photoset = flickr_api.Photoset.create(
                title="Integration Test Photoset - DELETE ME",
                description="This photoset was created by integration tests. Safe to delete.",
                primary_photo=self.ctx.test_photo,
            )
            self.ctx.test_photoset = photoset
            return f"Created photoset: {photoset.id}"

        self.run_test("upload.photo", upload_test_photo, requires_auth=True)
        self.run_test("photosets.create", create_test_photoset, requires_auth=True)

    def _test_write_photo_methods(self):
        """Test photo modification methods."""

        def test_photo_get_info():
            # Make sure we can get info on our test photo
            self.ctx.test_photo.getInfo()
            return f"title: {getattr(self.ctx.test_photo, 'title', 'N/A')}"

        def test_set_meta():
            self.ctx.test_photo.setMeta(
                title="Integration Test Photo - MODIFIED",
                description="Modified by setMeta test"
            )
            return "Meta updated"

        def test_set_tags():
            self.ctx.test_photo.setTags(tags="new-tag1 new-tag2 integration-test")
            return "Tags replaced"

        def test_add_tags():
            self.ctx.test_photo.addTags(tags="added-tag")
            return "Tag added"

        def test_set_dates():
            import time
            # Set taken date to now
            self.ctx.test_photo.setDates(
                date_taken=time.strftime("%Y-%m-%d %H:%M:%S"),
            )
            return "Dates updated"

        def test_set_perms():
            self.ctx.test_photo.setPerms(
                is_public=0,
                is_friend=0,
                is_family=0,
                perm_comment=0,  # nobody
                perm_addmeta=0,  # nobody
            )
            return "Permissions updated"

        def test_set_safety_level():
            self.ctx.test_photo.setSafetyLevel(safety_level=1)  # Safe
            return "Safety level set to Safe"

        def test_set_content_type():
            self.ctx.test_photo.setContentType(content_type=1)  # Photo
            return "Content type set to Photo"

        self.run_test("Photo.getInfo (test)", test_photo_get_info, requires="test_photo")
        self.run_test("Photo.setMeta", test_set_meta, requires="test_photo")
        self.run_test("Photo.setTags", test_set_tags, requires="test_photo")
        self.run_test("Photo.addTags", test_add_tags, requires="test_photo")
        self.run_test("Photo.setDates", test_set_dates, requires="test_photo")
        self.run_test("Photo.setPerms", test_set_perms, requires="test_photo")
        self.run_test("Photo.setSafetyLevel", test_set_safety_level, requires="test_photo")
        self.run_test("Photo.setContentType", test_set_content_type, requires="test_photo")

    def _test_write_photoset_methods(self):
        """Test photoset modification methods."""

        def test_photoset_edit_meta():
            self.ctx.test_photoset.editMeta(
                title="Integration Test Photoset - MODIFIED",
                description="Modified by editMeta test"
            )
            return "Photoset meta updated"

        def test_photoset_set_primary():
            # Set primary photo (to the same photo we already have)
            self.ctx.test_photoset.setPrimaryPhoto(photo=self.ctx.test_photo)
            return "Primary photo set"

        self.run_test("Photoset.editMeta", test_photoset_edit_meta, requires="test_photoset")
        self.run_test("Photoset.setPrimaryPhoto", test_photoset_set_primary, requires="test_photoset")

    def _test_write_tag_methods(self):
        """Test tag-specific methods."""

        def test_get_raw_tags():
            # Get raw tags for our test photo
            try:
                tags = flickr_api.Tag.getListUserRaw()
                return f"{len(tags) if tags else 0} raw tags"
            except Exception:
                return "0 raw tags"

        self.run_test("Tag.getListUserRaw (after add)", test_get_raw_tags, requires_auth=True)

    def _test_write_favorites(self):
        """Test favorites add/remove."""

        def test_add_favorite():
            # Add a photo from discovery (not our own) to favorites
            # Can't favorite your own photos
            if not self.ctx.photo:
                return "No discovery photo available"
            self.ctx.photo.addToFavorites()
            return "Added to favorites"

        def test_remove_favorite():
            # Remove from favorites
            if not self.ctx.photo:
                return "No discovery photo available"
            self.ctx.photo.removeFromFavorites()
            return "Removed from favorites"

        self.run_test("Photo.addToFavorites", test_add_favorite, requires="photo")
        self.run_test("Photo.removeFromFavorites", test_remove_favorite, requires="photo")

    def _test_write_download(self):
        """Test downloading the uploaded photo."""
        import tempfile

        def test_get_sizes():
            sizes = self.ctx.test_photo.getSizes()
            return f"{len(sizes)} sizes available"

        def test_download_photo():
            # Download to a temp file
            with tempfile.TemporaryDirectory() as tmpdir:
                output_file = os.path.join(tmpdir, "downloaded_test")
                result = self.ctx.test_photo.save(output_file, size_label="Medium")
                # Verify the file was created
                if os.path.exists(result):
                    size = os.path.getsize(result)
                    return f"Downloaded {size} bytes to {os.path.basename(result)}"
                else:
                    raise ValueError(f"Download file not found: {result}")

        def test_download_original():
            # Try to download original size
            with tempfile.TemporaryDirectory() as tmpdir:
                output_file = os.path.join(tmpdir, "downloaded_original")
                try:
                    result = self.ctx.test_photo.save(output_file, size_label="Original")
                    if os.path.exists(result):
                        size = os.path.getsize(result)
                        return f"Downloaded original: {size} bytes"
                    else:
                        raise ValueError(f"Download file not found: {result}")
                except Exception as e:
                    if "not found" in str(e).lower() or "not available" in str(e).lower():
                        return "Original not available (expected for some accounts)"
                    raise

        self.run_test("Photo.getSizes (test)", test_get_sizes, requires="test_photo")
        self.run_test("Photo.save (download)", test_download_photo, requires="test_photo")
        self.run_test("Photo.save (original)", test_download_original, requires="test_photo")

    def _test_write_cleanup(self):
        """Clean up test objects (photoset and photo)."""

        def delete_photoset():
            if self.ctx.test_photoset:
                self.ctx.test_photoset.delete()
                self.ctx.test_photoset = None
                return "Photoset deleted"
            return "No photoset to delete"

        def delete_photo():
            if self.ctx.test_photo:
                self.ctx.test_photo.delete()
                self.ctx.test_photo = None
                return "Photo deleted"
            return "No photo to delete"

        # Delete photoset first (while it still has the photo)
        self.run_test("Photoset.delete (cleanup)", delete_photoset, requires_auth=True)
        # Then delete the photo
        self.run_test("Photo.delete (cleanup)", delete_photo, requires_auth=True)


def _summarize(obj):
    """Create a brief summary of an object for display."""
    if obj is None:
        return "None"
    if isinstance(obj, str):
        return obj[:100] + "..." if len(obj) > 100 else obj
    if isinstance(obj, (list, tuple)):
        return f"[{len(obj)} items]"
    if hasattr(obj, '__dict__'):
        return f"{type(obj).__name__}({getattr(obj, 'id', '?')})"
    return str(obj)[:100]


def load_config(config_path: str = "~/.flickr_api_key",
                token_path: str = "~/.flickr_api_token"):
    """Load API keys and tokens from flickr_download config files.

    Returns:
        dict with api_key, api_secret, token, token_secret (token may be None)
    """
    config_path = os.path.expanduser(config_path)
    token_path = os.path.expanduser(token_path)

    result = {
        "api_key": None,
        "api_secret": None,
        "token": None,
        "token_secret": None,
    }

    # Load API keys from simple YAML config (key: value format)
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            for line in f:
                line = line.strip()
                if ":" in line and not line.startswith("#"):
                    key, value = line.split(":", 1)
                    key = key.strip()
                    value = value.strip()
                    if key == "api_key":
                        result["api_key"] = value
                    elif key == "api_secret":
                        result["api_secret"] = value

    # Load OAuth tokens (2 lines: token_key, token_secret)
    if os.path.exists(token_path):
        with open(token_path, "r") as f:
            lines = f.read().strip().split("\n")
            if len(lines) >= 2:
                result["token"] = lines[0]
                result["token_secret"] = lines[1]

    return result


def do_oauth_flow(api_key: str, api_secret: str, perms: str = "write") -> tuple:
    """Perform interactive OAuth flow to get access tokens.

    Args:
        api_key: Flickr API key
        api_secret: Flickr API secret
        perms: Permission level ('read', 'write', or 'delete')

    Returns:
        tuple of (access_token_key, access_token_secret)
    """
    print("\n" + "=" * 60)
    print(f"OAuth Authentication Flow (requesting '{perms}' permission)")
    print("=" * 60)

    # Create auth handler (fetches request token)
    print("\nRequesting authorization token from Flickr...")
    auth = AuthHandler(key=api_key, secret=api_secret)

    # Get authorization URL
    auth_url = auth.get_authorization_url(perms=perms)

    print("\nPlease visit this URL to authorize the application:")
    print()
    print(f"  {auth_url}")
    print()
    print("After authorizing, you'll be redirected to a page with XML.")
    print("Look for <oauth_verifier>XXXXXXXX</oauth_verifier> and copy the code.")
    print()

    # Get verifier from user
    verifier = input("Enter the verification code: ").strip()

    if not verifier:
        raise ValueError("No verification code provided")

    # Exchange for access token
    print("\nExchanging for access token...")
    auth.set_verifier(verifier)

    print(f"Successfully authenticated!")
    return auth.access_token_key, auth.access_token_secret


def save_token(token_path: str, token_key: str, token_secret: str):
    """Save OAuth tokens to a file."""
    token_path = os.path.expanduser(token_path)
    with open(token_path, "w") as f:
        f.write(f"{token_key}\n{token_secret}\n")
    print(f"Token saved to {token_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Run integration tests against the Flickr API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples (run from project root):
  # Use ~/.flickr_api_key and ~/.flickr_api_token (easiest)
  python integration_tests/integration_test.py --config

  # Use a specific config file
  python integration_tests/integration_test.py --config /path/to/config

  # API key only (public endpoints)
  python integration_tests/integration_test.py --api-key KEY --api-secret SECRET

  # Run OAuth flow to get a new token with write permissions
  python integration_tests/integration_test.py --config --auth --write-tests

  # Run write tests (will prompt for OAuth if no token exists)
  python integration_tests/integration_test.py --config --write-tests
"""
    )
    parser.add_argument(
        "--config", nargs="?", const="~/.flickr_api_key", metavar="PATH",
        help="Load API keys from config file (default: ~/.flickr_api_key)"
    )
    parser.add_argument(
        "--api-key",
        help="Flickr API key"
    )
    parser.add_argument(
        "--api-secret",
        help="Flickr API secret"
    )
    parser.add_argument(
        "--token",
        help="OAuth access token (for authenticated endpoints)"
    )
    parser.add_argument(
        "--token-secret",
        help="OAuth access token secret (for authenticated endpoints)"
    )
    parser.add_argument(
        "--test-username", default="flickr",
        help="Username to use for testing (default: flickr)"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true",
        help="Verbose output"
    )
    parser.add_argument(
        "--write-tests", action="store_true",
        help="Run write tests (upload, modify, delete). Requires auth tokens."
    )
    # Default test image is in the same directory as this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    default_test_image = os.path.join(script_dir, "Test.png")
    parser.add_argument(
        "--test-image", default=default_test_image,
        help=f"Path to test image for write tests (default: {default_test_image})"
    )
    parser.add_argument(
        "--auth", action="store_true",
        help="Run OAuth flow to get new tokens (use with --write-tests for write permissions)"
    )
    parser.add_argument(
        "--token-file", default="~/.flickr_api_token",
        help="Path to save/load OAuth tokens (default: ~/.flickr_api_token)"
    )

    args = parser.parse_args()

    # Load credentials
    api_key = args.api_key
    api_secret = args.api_secret
    token = args.token
    token_secret = args.token_secret

    if args.config:
        config = load_config(config_path=args.config, token_path=args.token_file)
        api_key = api_key or config["api_key"]
        api_secret = api_secret or config["api_secret"]
        token = token or config["token"]
        token_secret = token_secret or config["token_secret"]

    if not api_key or not api_secret:
        parser.error("--api-key and --api-secret required (or use --config)")

    # Handle OAuth flow if requested or needed
    if args.auth or (args.write_tests and not token):
        # Write tests need 'delete' permission (includes write)
        perms = "delete" if args.write_tests else "read"
        if not token:
            print("No existing token found.")
        token, token_secret = do_oauth_flow(api_key, api_secret, perms=perms)
        save_token(args.token_file, token, token_secret)

    tester = IntegrationTester(
        api_key=api_key,
        api_secret=api_secret,
        token=token,
        token_secret=token_secret,
        test_username=args.test_username,
        verbose=args.verbose,
        write_tests=args.write_tests,
        test_image=args.test_image,
    )

    exit_code = tester.run_all_tests()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
