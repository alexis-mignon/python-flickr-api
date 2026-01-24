# API Reference

This document provides a complete reference for all classes and methods in the python-flickr-api library.

## Table of Contents

- [Getting Started](#getting-started)
- [Core Classes](#core-classes)
  - [Photo](#photo)
  - [Person](#person)
  - [Photoset](#photoset)
  - [Gallery](#gallery)
  - [Group](#group)
  - [Collection](#collection)
  - [Tag](#tag)
  - [Place](#place)
- [Utility Classes](#utility-classes)
  - [Walker](#walker)
  - [FlickrList](#flickrlist)
  - [License](#license)
  - [Contact](#contact)
  - [Camera](#camera)
- [Statistics & Preferences](#statistics--preferences)
  - [stats](#stats)
  - [prefs](#prefs)
  - [Activity](#activity)
- [Other Classes](#other-classes)
  - [Blog](#blog)
  - [MachineTag](#machinetag)
  - [Panda](#panda)
  - [CommonInstitution](#commoninstitution)
  - [Reflection](#reflection)
  - [test](#test)
- [Module Functions](#module-functions)
  - [Upload Functions](#upload-functions)
  - [Cache Control](#cache-control)
  - [Direct API Access](#direct-api-access)

---

## Getting Started

### Two Ways to Access the API

The library provides two approaches:

#### 1. Object-Oriented Interface (Recommended)

```python
import flickr_api

flickr_api.set_keys(api_key="...", api_secret="...")

# Work with domain objects
user = flickr_api.Person.findByUserName("username")
photos = user.getPublicPhotos()

for photo in photos:
    print(photo.title)
```

#### 2. Direct REST API Access

```python
from flickr_api.api import flickr

# Call Flickr API methods directly
response = flickr.photos.search(tags="sunset", per_page=10)
```

### Flexible Arguments

Most methods accept either object instances or ID strings:

```python
# Using an object
photo.addTag(tag=tag_object)

# Using an ID
photo.addTag(tag_id="12345")
```

### Photo Size Labels

When downloading or getting photo URLs, use these size labels:

| Label | Typical Size |
|-------|--------------|
| Square | 75x75 |
| Large Square | 150x150 |
| Thumbnail | 100 on longest side |
| Small | 240 on longest side |
| Small 320 | 320 on longest side |
| Medium | 500 on longest side |
| Medium 640 | 640 on longest side |
| Medium 800 | 800 on longest side |
| Large | 1024 on longest side |
| Large 1600 | 1600 on longest side |
| Large 2048 | 2048 on longest side |
| Original | Original dimensions |

---

## Core Classes

### Photo

The primary class for working with Flickr photos.

#### Getting Photos

```python
# Search for photos
photos = flickr_api.Photo.search(tags="nature", per_page=20)

# Get recent public photos
recent = flickr_api.Photo.getRecent()

# Get interesting photos
interesting = flickr_api.Photo.getInteresting()

# Get a specific photo by ID
photo = flickr_api.Photo(id="photo_id")
photo.getInfo()  # Load full details
```

#### Photo Information

| Method | Description |
|--------|-------------|
| `getInfo()` | Load detailed photo information |
| `getSizes(force=False)` | Get available sizes with URLs and dimensions |
| `getExif()` | Get EXIF metadata |
| `getContext()` | Get previous/next photos in context |
| `getAllContexts()` | Get photosets and pools containing photo |
| `getPageUrl()` | Get Flickr page URL |
| `getPhotoUrl(size_label=None)` | Get URL to photo page for size |
| `getPhotoFile(size_label=None)` | Get direct URL to image file |

#### Downloading Photos

```python
# Save to file
photo.save("photo.jpg", size_label="Large")

# Save with custom timeout
photo.save("photo.jpg", size_label="Original", timeout=30)

# Display using PIL (requires Pillow)
photo.show(size_label="Medium 640")
```

#### Tags

| Method | Description |
|--------|-------------|
| `getTags()` | Get all tags on the photo |
| `addTags(tags)` | Add tags (list or comma-separated string) |
| `setTags(tags)` | Replace all tags |
| `removeTag(tag_id=...)` | Remove a specific tag |

```python
photo.addTags(["nature", "sunset", "landscape"])
photo.addTags("nature, sunset, landscape")  # Also works

tags = photo.getTags()
for tag in tags:
    print(tag.text)
```

#### Comments

| Method | Description |
|--------|-------------|
| `getComments()` | Get comments on the photo |
| `addComment(comment_text="...")` | Add a comment |

```python
photo.addComment(comment_text="Beautiful shot!")

comments = photo.getComments()
for comment in comments:
    print(f"{comment.author.username}: {comment.text}")

# Delete or edit a comment
comment.delete()
comment.edit(comment_text="Updated text")
```

#### Notes (Regions)

```python
# Add a note to a region of the photo
photo.addNote(
    note_x=10, note_y=10,
    note_w=100, note_h=100,
    note_text="This is a note"
)

# Edit or delete notes
note.edit(note_text="Updated")
note.delete()
```

#### People Tags

| Method | Description |
|--------|-------------|
| `getPeople()` | Get tagged people |
| `addPerson(user_id=..., ...)` | Tag a person |
| `deletePerson(user_id=...)` | Remove person tag |
| `editPersonCoords(...)` | Adjust tag coordinates |
| `deletePersonCoords(...)` | Remove coordinates |

#### Location

| Method | Description |
|--------|-------------|
| `getLocation()` | Get geolocation data |
| `setLocation(lat=..., lon=..., accuracy=...)` | Set geolocation |
| `removeLocation()` | Remove geolocation |
| `getGeoPerms()` | Get geolocation privacy settings |
| `setGeoPerms(...)` | Set geolocation privacy |

```python
location = photo.getLocation()
print(f"Lat: {location.latitude}, Lon: {location.longitude}")
```

#### Favorites

| Method | Description |
|--------|-------------|
| `getFavorites()` | Get users who favorited this photo |
| `addToFavorites()` | Add to your favorites |
| `removeFromFavorites()` | Remove from favorites |

#### Permissions & Metadata

| Method | Description |
|--------|-------------|
| `getPerms()` | Get photo permissions |
| `setPerms(is_public=..., is_friend=..., is_family=...)` | Set permissions |
| `setMeta(title=..., description=...)` | Set title/description |
| `setDates(date_posted=..., date_taken=...)` | Set dates |
| `setContentType(content_type=...)` | 1=Photo, 2=Screenshot, 3=Other |
| `setSafetyLevel(safety_level=...)` | 1=Safe, 2=Moderate, 3=Restricted |
| `setLicence(licence=...)` | Set Creative Commons license |

#### Other Operations

| Method | Description |
|--------|-------------|
| `delete()` | Delete the photo |
| `rotate(degrees=...)` | Rotate by 90, 180, or 270 degrees |
| `getStats(date)` | Get view statistics for a date |
| `getGalleries()` | Get galleries containing this photo |

#### Static Search Methods

```python
# Full-text and tag search
flickr_api.Photo.search(
    text="sunset beach",
    tags="nature,ocean",
    tag_mode="all",  # "all" or "any"
    user_id="user_id",
    min_upload_date="2023-01-01",
    per_page=100
)

# Get photos by criteria
flickr_api.Photo.getRecent()
flickr_api.Photo.getInteresting()
flickr_api.Photo.getUntagged()
flickr_api.Photo.getWithGeoData()
flickr_api.Photo.getWithoutGeoData()
flickr_api.Photo.recentlyUpdated(min_date="2023-01-01")
```

---

### Person

Represents a Flickr user.

#### Finding Users

```python
# By username
user = flickr_api.Person.findByUserName("username")

# By email
user = flickr_api.Person.findByEmail("user@example.com")

# By profile URL
user = flickr_api.Person.findByUrl("https://www.flickr.com/photos/username/")

# Currently authenticated user
user = flickr_api.Person.getFromToken()
# Or
user = flickr_api.test.login()
```

#### User Information

| Method | Description |
|--------|-------------|
| `getInfo()` | Get profile information |
| `getPhotosUrl()` | Get URL to photo stream |
| `getProfileUrl()` | Get URL to profile page |
| `getLimits()` | Get upload limits |

```python
user.getInfo()
print(f"Username: {user.username}")
print(f"Real name: {user.realname}")
print(f"Location: {user.location}")
```

#### User's Photos

| Method | Description |
|--------|-------------|
| `getPhotos()` | Get user's photos (requires auth for private) |
| `getPublicPhotos()` | Get public photos |
| `getPhotosOf()` | Get photos where user is tagged |
| `getNotInSetPhotos()` | Get photos not in any photoset |
| `getFavorites()` | Get user's favorites |
| `getPublicFavorites()` | Get public favorites |

```python
photos = user.getPublicPhotos(per_page=50)
print(f"Total photos: {photos.info.total}")

for photo in photos:
    print(photo.title)
```

#### User's Collections

| Method | Description |
|--------|-------------|
| `getPhotosets()` | Get photosets/albums |
| `getGalleries()` | Get galleries |
| `getCollectionTree()` | Get collection hierarchy |
| `getPublicGroups()` | Get groups user belongs to |
| `getPublicContacts()` | Get contacts |

#### Tags

| Method | Description |
|--------|-------------|
| `getTags()` | Get all tags user has used |
| `getPopularTags(count=...)` | Get most-used tags |

---

### Photoset

Represents an album/photoset.

#### Creating and Managing Photosets

```python
# Create a new photoset
photoset = flickr_api.Photoset.create(
    title="My Album",
    description="Album description",
    primary_photo=photo  # or primary_photo_id="id"
)

# Get photoset info
photoset.getInfo()
print(f"Title: {photoset.title}")
print(f"Photo count: {photoset.count_photos}")

# Delete photoset
photoset.delete()
```

#### Photos in Photoset

| Method | Description |
|--------|-------------|
| `getPhotos(per_page=..., page=...)` | Get photos with pagination |
| `addPhoto(photo=...)` | Add a photo |
| `removePhoto(photo=...)` | Remove a photo |
| `removePhotos(photo_ids=...)` | Remove multiple photos |
| `editPhotos(primary_photo_id=..., photo_ids=...)` | Set contents and order |
| `reorderPhotos(photo_ids=...)` | Reorder photos |
| `setPrimaryPhoto(photo=...)` | Set cover photo |

```python
photos = photoset.getPhotos()
for photo in photos:
    print(photo.title)

# Add photo to photoset
photoset.addPhoto(photo=my_photo)
```

#### Metadata

| Method | Description |
|--------|-------------|
| `editMeta(title=..., description=...)` | Update title/description |
| `getContext(photo=...)` | Get prev/next photo in set |
| `getStats(date)` | Get view statistics |

#### Comments

```python
photoset.addComment(comment_text="Great collection!")
comments = photoset.getComments()

# Edit or delete
comment.edit(comment_text="Updated")
comment.delete()
```

---

### Gallery

Curated collection of photos from any Flickr user.

#### Creating Galleries

```python
gallery = flickr_api.Gallery.create(
    title="My Gallery",
    description="Curated photos"
)
```

#### Gallery Operations

| Method | Description |
|--------|-------------|
| `getInfo()` | Get gallery details |
| `getPhotos(per_page=...)` | Get photos in gallery |
| `addPhoto(photo=...)` | Add a photo |
| `editPhoto(photo=..., comment=...)` | Edit photo in gallery |
| `editPhotos(...)` | Update multiple photos |
| `editMedia(title=..., description=...)` | Update metadata |

```python
# Get gallery by URL
gallery = flickr_api.Gallery.getByUrl(
    "https://www.flickr.com/photos/user/galleries/id/"
)

photos = gallery.getPhotos()
```

---

### Group

Represents a Flickr group/pool.

#### Finding Groups

```python
# Search for groups
groups = flickr_api.Group.search(text="photography")

# Get by URL
group = flickr_api.Group.getByUrl(
    "https://www.flickr.com/groups/groupname/"
)

# Get user's groups
my_groups = flickr_api.Group.getGroups()
```

#### Group Information

| Method | Description |
|--------|-------------|
| `getInfo()` | Get group details |
| `getMembers(per_page=...)` | Get members |
| `getUrl()` | Get Flickr URL |

#### Group Pool

| Method | Description |
|--------|-------------|
| `getPhotos(per_page=...)` | Get photos in pool |
| `addPhoto(photo=...)` | Add photo to pool |
| `removePhoto(photo=...)` | Remove from pool |
| `getPoolContext(photo=...)` | Get prev/next in pool |

```python
photos = group.getPhotos(per_page=50)
group.addPhoto(photo=my_photo)
```

#### Group Membership

| Method | Description |
|--------|-------------|
| `join()` | Join the group |
| `leave()` | Leave the group |
| `joinRequest(message=...)` | Request to join |

#### Discussions

```python
# Get discussion topics
topics = group.getDiscussTopics()

# Create a topic
group.addDiscussTopic(subject="Topic title", message="Content")

# Get replies
topic.getReplies()
topic.addReply(message="My reply")
```

---

### Collection

Hierarchical organization of photosets.

```python
# Get user's collection tree
tree = user.getCollectionTree()

# Get collection info
collection.getInfo()
print(f"Title: {collection.title}")
print(f"Sets: {collection.sets}")

# Get statistics
collection.getStats(date="2023-01-01")
```

---

### Tag

Represents tags on photos.

#### Working with Tags

```python
# Get tags on a photo
tags = photo.getTags()
for tag in tags:
    print(f"{tag.text} (raw: {tag.raw})")

# Remove a tag
tag.remove()
```

#### Static Methods

| Method | Description |
|--------|-------------|
| `Tag.getHotList(period=..., count=...)` | Get trending tags |
| `Tag.getRelated(tag="...")` | Get related tags |
| `Tag.getListUser(user_id=...)` | Get user's tags |
| `Tag.getListUserPopular(user_id=..., count=...)` | Get user's popular tags |
| `Tag.getClusters(tag="...")` | Get tag clusters |

```python
hot_tags = flickr_api.Tag.getHotList(period="day", count=20)
related = flickr_api.Tag.getRelated(tag="sunset")
```

#### Tag Clusters

```python
clusters = flickr_api.Tag.getClusters(tag="apple")
for cluster in clusters:
    photos = cluster.getPhotos()
```

---

### Place

Geographic locations on Flickr.

#### Finding Places

```python
# Search by name
places = flickr_api.Place.find(query="Paris, France")

# Find by coordinates
place = flickr_api.Place.findByLatLon(lat=48.8566, lon=2.3522)

# Get by URL
place = flickr_api.Place.getByUrl("...")
```

#### Place Information

| Method | Description |
|--------|-------------|
| `getInfo()` | Get place details |
| `getChildrenWithPhotoPublic()` | Get child places with photos |
| `getTags()` | Get popular tags for place |
| `getTopPlaces(place_type_id=...)` | Get top places |

```python
place.getInfo()
print(f"Name: {place.name}")
print(f"Type: {place.place_type}")  # city, county, region, country
```

#### Static Methods

| Method | Description |
|--------|-------------|
| `Place.getPlaceTypes()` | Get place type definitions |
| `Place.placesForBoundingBox(...)` | Find places in bounding box |
| `Place.placesForTags(...)` | Find places for tags |
| `Place.placesForUser(...)` | Get places from user's photos |

---

## Utility Classes

### Walker

Automatically handles pagination when iterating through large result sets.

```python
from flickr_api import Walker

# Create a walker for any method that returns paginated results
walker = Walker(flickr_api.Photo.search, tags="nature")

# Iterate through ALL results (handles pagination automatically)
for photo in walker:
    print(photo.title)

# Get total count
print(f"Total results: {len(walker)}")

# Use slicing to limit results
for photo in walker[:100]:  # First 100 only
    print(photo.title)
```

Works with any method that returns `FlickrList`:
- `Photo.search()`
- `user.getPhotos()`
- `photoset.getPhotos()`
- `group.getPhotos()`
- etc.

---

### FlickrList

List wrapper with pagination information. Returned by most methods that return multiple items.

```python
photos = user.getPublicPhotos(per_page=50)

# Access items
for photo in photos:
    print(photo.title)

# Access pagination info
print(f"Page: {photos.info.page}")
print(f"Per page: {photos.info.perpage}")
print(f"Total pages: {photos.info.pages}")
print(f"Total items: {photos.info.total}")
```

---

### License

Creative Commons and other license types.

```python
# Get all available licenses
licenses = flickr_api.License.getList()

for lic in licenses:
    print(f"{lic.id}: {lic.name} - {lic.url}")

# Set license on a photo
photo.setLicence(licence=license_object)
# Or by ID
photo.setLicence(licence_id=4)  # Attribution License
```

---

### Contact

User contacts/friends.

```python
# Get your contacts
contacts = flickr_api.Contact.getList()

# Get recently active contacts
recent = flickr_api.Contact.getListRecentlyUploaded()

# Get tagging suggestions
suggestions = flickr_api.Contact.getTaggingSuggestions()
```

---

### Camera

Camera equipment information.

```python
# Get camera brands
brands = flickr_api.Camera.Brand.getList()

for brand in brands:
    print(brand.name)
    models = brand.getModels()
    for model in models:
        print(f"  {model.name}")
```

---

## Statistics & Preferences

### stats

Access view statistics and analytics (requires authentication).

```python
from flickr_api import stats

# Get photo statistics for a date
photo_stats = stats.getPhotoStats(date="2023-01-15", photo_id="...")

# Get popular photos
popular = stats.getPopularPhotos()

# Get total views
totals = stats.getTotalViews()

# Get referrer information
domains = stats.getPhotoDomains(date="2023-01-15")
referrers = stats.getPhotoReferrers(date="2023-01-15", domain="google.com")

# Also available for photosets, collections, and photostream
stats.getPhotosetStats(date="...", photoset_id="...")
stats.getCollectionStats(date="...", collection_id="...")
stats.getPhotostreamStats(date="...")

# Download CSV reports
csv_files = stats.getCSVFiles()
```

---

### prefs

Get user preferences.

```python
from flickr_api import prefs

# Get various preferences
content_type = prefs.getContentType()
geo_perms = prefs.getGeoPerms()
hidden = prefs.getHidden()
privacy = prefs.getPrivacy()
safety = prefs.getSafetyLevel()
```

---

### Activity

Activity streams showing recent activity.

```python
from flickr_api import Activity

# Get activity on your photos
activity = Activity.userPhotos(timeframe="7d")

# Get activity on photos you've commented on
comments_activity = Activity.userComments(per_page=50)
```

---

## Other Classes

### Blog

Post photos to linked blog services.

```python
# Get linked blogs
blogs = flickr_api.BlogService.getList()

# Post a photo to a blog
blog.postPhoto(
    photo=photo,
    title="Post title",
    description="Post content"
)

# Get available blog services
services = flickr_api.BlogService.getServices()
```

---

### MachineTag

Machine tags with namespaces and predicates (e.g., `geo:lat=48.8566`).

```python
from flickr_api import MachineTag

# Get namespaces
namespaces = MachineTag.getNamespaces()

# Get namespace:predicate pairs
pairs = MachineTag.getPairs(namespace="geo")

# Get predicates
predicates = MachineTag.getPredicates(namespace="geo")

# Get values
values = MachineTag.getValues(namespace="geo", predicate="lat")
```

---

### Panda

The Flickr Panda feature for exploring photos.

```python
from flickr_api import Panda

# Get available pandas
pandas = Panda.getList()

# Get photos from a panda
for panda in pandas:
    photos = panda.getPhotos()
```

---

### CommonInstitution

Libraries and museums participating in Flickr Commons.

```python
institutions = flickr_api.CommonInstitution.getInstitutions()

for inst in institutions:
    print(f"{inst.name}: {inst.nsid}")
```

---

### Reflection

Introspect available Flickr API methods.

```python
from flickr_api import Reflection

# Get all available methods
methods = Reflection.getMethods()

# Get info about a specific method
info = Reflection.getMethodInfo(method_name="flickr.photos.search")
print(info.description)
```

---

### test

Testing and utility methods.

```python
from flickr_api import test

# Test authentication
user = test.login()
print(f"Logged in as: {user.username}")

# Echo test
result = test.echo(foo="bar")

# Null test
test.null()
```

---

## Module Functions

### Upload Functions

#### upload()

Upload a photo to Flickr.

```python
import flickr_api

# Basic upload
photo = flickr_api.upload(photo_file="/path/to/photo.jpg")

# With metadata
photo = flickr_api.upload(
    photo_file="/path/to/photo.jpg",
    title="Photo Title",
    description="Photo description with <b>HTML</b>",
    tags="tag1 tag2 tag3",
    is_public=1,      # 0 or 1
    is_friend=0,
    is_family=0,
    safety_level=1,   # 1=Safe, 2=Moderate, 3=Restricted
    content_type=1,   # 1=Photo, 2=Screenshot, 3=Other
    hidden=1          # 1=Show in search, 2=Hide from search
)

# Async upload (returns ticket for status checking)
ticket = flickr_api.upload(
    photo_file="/path/to/photo.jpg",
    asynchronous=1
)

# Check upload status
status = flickr_api.Photo.checkUploadTickets(tickets=[ticket])
```

#### replace()

Replace an existing photo's image file.

```python
# Replace photo image
photo = flickr_api.replace(
    photo_file="/path/to/new_photo.jpg",
    photo=existing_photo  # or photo_id="id"
)

# Async replace
ticket = flickr_api.replace(
    photo_file="/path/to/new_photo.jpg",
    photo_id="12345",
    asynchronous=1
)
```

---

### Cache Control

Enable caching to reduce repeated API calls.

```python
import flickr_api

# Enable with defaults (200 entries, 300s timeout)
flickr_api.enable_cache()

# Enable with custom settings
from flickr_api.cache import SimpleCache
flickr_api.enable_cache(SimpleCache(timeout=600, max_entries=500))

# Disable caching
flickr_api.disable_cache()
```

---

### Timeout Control

Set HTTP request timeout.

```python
import flickr_api

# Set timeout in seconds (default: 10)
flickr_api.set_timeout(30)

# Get current timeout
current = flickr_api.get_timeout()
```

---

### Direct API Access

For advanced use or methods not wrapped by the library.

```python
from flickr_api.api import flickr

# Call any Flickr API method directly
response = flickr.photos.search(
    tags="sunset",
    per_page=10,
    format="json"
)

# Returns parsed JSON/XML response
response = flickr.reflection.getMethodInfo(
    method_name="flickr.photos.getInfo"
)
```

The method hierarchy mirrors the Flickr API:
- `flickr.photos.*`
- `flickr.people.*`
- `flickr.photosets.*`
- `flickr.groups.*`
- etc.

---

## Common Patterns

### Iterating Through All Results

```python
from flickr_api import Walker

# Walker handles pagination automatically
for photo in Walker(flickr_api.Photo.search, tags="nature"):
    process(photo)
```

### Error Handling

```python
from flickr_api.flickrerrors import FlickrError

try:
    photo = flickr_api.Photo(id="invalid")
    photo.getInfo()
except FlickrError as e:
    print(f"Flickr API error: {e}")
```

### Checking Permissions

```python
# Check if photo is public before processing
if photo.ispublic:
    print("Public photo")

# Check authentication status
try:
    user = flickr_api.test.login()
    print(f"Authenticated as {user.username}")
except:
    print("Not authenticated")
```
