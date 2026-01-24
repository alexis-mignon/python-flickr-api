"""
Tests for Place API methods.

Batch 19:
flickr.places.find, flickr.places.findByLatLon,
flickr.places.getChildrenWithPhotosPublic, flickr.places.getInfo,
flickr.places.getInfoByUrl, flickr.places.getPlaceTypes,
flickr.places.getShapeHistory, flickr.places.getTopPlacesList,
flickr.places.placesForBoundingBox, flickr.places.placesForContacts

Batch 20:
flickr.places.placesForTags, flickr.places.placesForUser,
flickr.places.tagsForPlace

Uses example responses from the api-docs/ directory.
"""
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call

from base_test import FlickrApiTestCase
from test_utils import xml_to_flickr_json, load_api_doc


class TestPlaceMethods(FlickrApiTestCase):
    """Tests for Place API methods"""

    @patch.object(method_call.requests, "post")
    def test_place_find(self, mock_post):
        """Test Place.find (flickr.places.find)"""
        api_doc = load_api_doc("flickr.places.find")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        places = f.Place.find(query="Alabama")

        # Verify we got 3 places
        self.assertEqual(len(places), 3)

        # First place - Alabama region
        p1 = places[0]
        self.assertIsInstance(p1, f.Place)
        self.assertEqual(p1.id, "VrrjuESbApjeFS4.")
        self.assertEqual(p1.woeid, "2347559")
        self.assertEqual(p1.latitude, 32.614)
        self.assertEqual(p1.longitude, -86.680)
        self.assertEqual(p1.place_url, "/United+States/Alabama")
        self.assertEqual(p1.place_type, "region")
        self.assertEqual(p1.name, "Alabama, Alabama, United States")

        # Second place - Alabama, New York
        p2 = places[1]
        self.assertEqual(p2.id, "cGHuc0mbApmzEHoP")
        self.assertEqual(p2.place_type, "locality")

        # Third place - Alabama, South Africa
        p3 = places[2]
        self.assertEqual(p3.id, "o4yVPEqYBJvFMP8Q")

        # Verify pagination info
        self.assertEqual(places.info.total, 3)

    @patch.object(method_call.requests, "post")
    def test_place_find_by_lat_lon(self, mock_post):
        """Test Place.findByLatLon (flickr.places.findByLatLon)"""
        api_doc = load_api_doc("flickr.places.findByLatLon")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        places = f.Place.findByLatLon(lat=37.76513, lon=-122.42020)

        # Verify we got 1 place
        self.assertEqual(len(places), 1)

        # Mission Dolores neighbourhood
        p1 = places[0]
        self.assertIsInstance(p1, f.Place)
        self.assertEqual(p1.id, "Y12JWsKbApmnSQpbQg")
        self.assertEqual(p1.woeid, "23512048")
        self.assertEqual(p1.latitude, 37.765)
        self.assertEqual(p1.longitude, -122.424)
        self.assertEqual(
            p1.place_url,
            "/United+States/California/San+Francisco/Mission+Dolores"
        )
        self.assertEqual(p1.place_type, "neighbourhood")
        self.assertEqual(p1.place_type_id, "22")
        self.assertEqual(p1.timezone, "America/Los_Angeles")
        self.assertEqual(
            p1.name,
            "Mission Dolores, San Francisco, CA, US, United States"
        )

        # Verify pagination info
        self.assertEqual(places.info.total, 1)

    @patch.object(method_call.requests, "post")
    def test_place_get_children_with_photo_public(self, mock_post):
        """Test Place.getChildrenWithPhotoPublic
        (flickr.places.getChildrenWithPhotosPublic)"""
        api_doc = load_api_doc("flickr.places.getChildrenWithPhotosPublic")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        # Montreal place
        place = f.Place(id="4hLQygSaBJ92")
        children = place.getChildrenWithPhotoPublic()

        # Verify we got 2 places
        self.assertEqual(len(children), 2)

        # First child - Montreal Golden Square Mile
        c1 = children[0]
        self.assertIsInstance(c1, f.Place)
        self.assertEqual(c1.id, "HznQfdKbB58biy8sdA")
        self.assertEqual(c1.woeid, "26332794")
        self.assertEqual(c1.latitude, 45.498)
        self.assertEqual(c1.longitude, -73.575)
        self.assertEqual(c1.place_type, "neighbourhood")
        self.assertEqual(c1.photo_count, "2717")

        # Second child - Downtown Montreal
        c2 = children[1]
        self.assertEqual(c2.id, "K1rYWmGbB59rwn7lOA")
        self.assertEqual(c2.photo_count, "2317")

        # Verify pagination info
        self.assertEqual(children.info.total, 79)

    @patch.object(method_call.requests, "post")
    def test_place_get_info(self, mock_post):
        """Test Place.getInfo (flickr.places.getInfo)"""
        api_doc = load_api_doc("flickr.places.getInfo")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        place = f.Place(id="4hLQygSaBJ92")
        result = place.getInfo()

        # getInfo returns a dict of properties (used by lazy loading)
        # Note: converters don't run on the raw dict, so lat/lon are strings
        self.assertIsInstance(result, dict)
        self.assertEqual(result["id"], "4hLQygSaBJ92")
        self.assertEqual(result["woeid"], "3534")
        self.assertEqual(result["latitude"], "45.512")
        self.assertEqual(result["longitude"], "-73.554")
        self.assertEqual(result["place_url"], "/Canada/Quebec/Montreal")
        self.assertEqual(result["place_type"], "locality")
        self.assertEqual(result["has_shapedata"], 1)
        self.assertEqual(result["timezone"], "America/Toronto")

        # Nested locality
        self.assertIsInstance(result["locality"], f.Place)
        self.assertEqual(result["locality"].id, "4hLQygSaBJ92")
        self.assertEqual(result["locality"].name, "Montreal")

        # Nested county
        self.assertIsInstance(result["county"], f.Place)
        self.assertEqual(result["county"].id, "cFBi9x6bCJ8D5rba1g")
        self.assertEqual(result["county"].name, "Montréal")

        # Nested region
        self.assertIsInstance(result["region"], f.Place)
        self.assertEqual(result["region"].id, "CrZUvXebApjI0.72")
        self.assertEqual(result["region"].name, "Quebec")

        # Nested country
        self.assertIsInstance(result["country"], f.Place)
        self.assertEqual(result["country"].id, "EESRy8qbApgaeIkbsA")
        self.assertEqual(result["country"].name, "Canada")

        # ShapeData
        self.assertIsInstance(result["shapedata"], f.Place.ShapeData)
        self.assertEqual(result["shapedata"].created, "1223513357")
        self.assertEqual(result["shapedata"].count_points, "34778")
        self.assertEqual(result["shapedata"].count_edges, "52")
        self.assertEqual(result["shapedata"].has_donuthole, 1)
        self.assertEqual(result["shapedata"].is_donuthole, 1)

        # ShapeData polylines
        self.assertIsInstance(result["shapedata"].polylines, list)
        self.assertEqual(len(result["shapedata"].polylines), 1)
        self.assertIsInstance(
            result["shapedata"].polylines[0],
            f.Place.ShapeData.Polyline
        )

    @patch.object(method_call.requests, "post")
    def test_place_get_by_url(self, mock_post):
        """Test Place.getByUrl (flickr.places.getInfoByUrl)"""
        api_doc = load_api_doc("flickr.places.getInfoByUrl")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        result = f.Place.getByUrl(url="/Canada/Quebec/Montreal")

        # Returns a Place object
        self.assertIsInstance(result, f.Place)
        self.assertEqual(result.id, "4hLQygSaBJ92")
        self.assertEqual(result.woeid, "3534")
        self.assertEqual(result.latitude, 45.512)
        self.assertEqual(result.longitude, -73.554)
        self.assertEqual(result.place_url, "/Canada/Quebec/Montreal")
        self.assertEqual(result.place_type, "locality")

        # Nested places
        self.assertIsInstance(result.locality, f.Place)
        self.assertIsInstance(result.county, f.Place)
        self.assertIsInstance(result.region, f.Place)
        self.assertIsInstance(result.country, f.Place)

        # ShapeData (without urls in this example)
        self.assertIsInstance(result.shapedata, f.Place.ShapeData)
        self.assertEqual(result.shapedata.created, "1223513357")

    @patch.object(method_call.requests, "post")
    def test_place_get_place_types(self, mock_post):
        """Test Place.getPlaceTypes (flickr.places.getPlaceTypes)"""
        api_doc = load_api_doc("flickr.places.getPlaceTypes")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        place_types = f.Place.getPlaceTypes()

        # Verify we got 6 place types
        self.assertEqual(len(place_types), 6)

        # Neighbourhood
        pt1 = place_types[0]
        self.assertIsInstance(pt1, f.Place.Type)
        self.assertEqual(pt1.id, "22")
        self.assertEqual(pt1.text, "neighbourhood")

        # Locality
        pt2 = place_types[1]
        self.assertEqual(pt2.id, "7")
        self.assertEqual(pt2.text, "locality")

        # County
        pt3 = place_types[2]
        self.assertEqual(pt3.id, "9")
        self.assertEqual(pt3.text, "county")

        # Region
        pt4 = place_types[3]
        self.assertEqual(pt4.id, "8")
        self.assertEqual(pt4.text, "region")

        # Country
        pt5 = place_types[4]
        self.assertEqual(pt5.id, "12")
        self.assertEqual(pt5.text, "country")

        # Continent
        pt6 = place_types[5]
        self.assertEqual(pt6.id, "29")
        self.assertEqual(pt6.text, "continent")

    @patch.object(method_call.requests, "post")
    def test_place_get_shape_history(self, mock_post):
        """Test Place.getShapeHistory (flickr.places.getShapeHistory)"""
        api_doc = load_api_doc("flickr.places.getShapeHistory")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        shapes = f.Place.getShapeHistory(place_id="4hLQygSaBJ92")

        # Verify we got 1 shapedata in example (despite "total=2" in response)
        self.assertEqual(len(shapes), 1)

        # First shapedata
        sd1 = shapes[0]
        self.assertIsInstance(sd1, f.Place.ShapeData)
        self.assertEqual(sd1.created, "1223513357")
        self.assertEqual(sd1.alpha, "0.012359619140625")
        self.assertEqual(sd1.count_points, "34778")
        self.assertEqual(sd1.count_edges, "52")
        self.assertEqual(sd1.is_donuthole, 0)

        # Polylines
        self.assertIsInstance(sd1.polylines, list)
        self.assertEqual(len(sd1.polylines), 1)
        self.assertIsInstance(sd1.polylines[0], f.Place.ShapeData.Polyline)

    @patch.object(method_call.requests, "post")
    def test_place_get_top_places(self, mock_post):
        """Test Place.getTopPlaces (flickr.places.getTopPlacesList)"""
        api_doc = load_api_doc("flickr.places.getTopPlacesList")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        place = f.Place(id="4KO02SibApitvSBieQ")
        top_places = place.getTopPlaces(place_type_id=12)

        # Verify we got 1 place in example
        self.assertEqual(len(top_places), 1)

        # United States
        p1 = top_places[0]
        self.assertIsInstance(p1, f.Place)
        self.assertEqual(p1.id, "4KO02SibApitvSBieQ")
        self.assertEqual(p1.woeid, "23424977")
        self.assertEqual(p1.latitude, 48.890)
        self.assertEqual(p1.longitude, -116.982)
        self.assertEqual(p1.place_url, "/United+States")
        self.assertEqual(p1.place_type, "country")
        self.assertEqual(p1.place_type_id, "12")
        self.assertEqual(p1.photo_count, "23371")
        self.assertEqual(p1.name, "United States")

        # Verify pagination info
        self.assertEqual(top_places.info.total, 100)

    @patch.object(method_call.requests, "post")
    def test_place_places_for_bounding_box(self, mock_post):
        """Test Place.placesForBoundingBox (flickr.places.placesForBoundingBox)
        """
        api_doc = load_api_doc("flickr.places.placesForBoundingBox")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        places = f.Place.placesForBoundingBox(
            bbox="-122.42307,37.773779,-122.381071,37.815779"
        )

        # Verify we got 3 places
        self.assertEqual(len(places), 3)

        # First place - Downtown
        p1 = places[0]
        self.assertIsInstance(p1, f.Place)
        self.assertEqual(p1.id, ".aaSwYSbApnq6seyGw")
        self.assertEqual(p1.woeid, "23512025")
        self.assertEqual(p1.latitude, 37.788)
        self.assertEqual(p1.longitude, -122.412)
        self.assertEqual(
            p1.place_url,
            "/United+States/California/San+Francisco/Downtown"
        )
        self.assertEqual(p1.place_type, "neighbourhood")

        # Second place - Civic Center
        p2 = places[1]
        self.assertEqual(p2.id, "3KymK1GbCZ41eBVBxg")

        # Third place - Chinatown
        p3 = places[2]
        self.assertEqual(p3.id, "9xdhxY.bAptvBjHo")

    @patch.object(method_call.requests, "post")
    def test_place_places_for_contacts(self, mock_post):
        """Test Place.placesForContacts (flickr.places.placesForContacts)"""
        api_doc = load_api_doc("flickr.places.placesForContacts")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        places = f.Place.placesForContacts(place_type_id=7)

        # Verify we got 1 place
        self.assertEqual(len(places), 1)

        # San Francisco
        p1 = places[0]
        self.assertIsInstance(p1, f.Place)
        self.assertEqual(p1.id, "kH8dLOubBZRvX_YZ")
        self.assertEqual(p1.woeid, "2487956")
        self.assertEqual(p1.latitude, 37.779)
        self.assertEqual(p1.longitude, -122.420)
        self.assertEqual(
            p1.place_url,
            "/United+States/California/San+Francisco"
        )
        self.assertEqual(p1.place_type, "locality")
        self.assertEqual(p1.photo_count, "156")
        self.assertEqual(p1.name, "San Francisco, California")

    @patch.object(method_call.requests, "post")
    def test_place_places_for_tags(self, mock_post):
        """Test Place.placesForTags (flickr.places.placesForTags)"""
        api_doc = load_api_doc("flickr.places.placesForTags")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        places = f.Place.placesForTags(
            place_type_id=7,
            place_id="4KO02SibApitvSBieQ",
            tags="sanfrancisco"
        )

        # Verify we got 1 place
        self.assertEqual(len(places), 1)

        # San Francisco
        p1 = places[0]
        self.assertIsInstance(p1, f.Place)
        self.assertEqual(p1.id, "kH8dLOubBZRvX_YZ")
        self.assertEqual(p1.woeid, "2487956")
        self.assertEqual(p1.latitude, 37.779)
        self.assertEqual(p1.longitude, -122.420)
        self.assertEqual(
            p1.place_url,
            "/United+States/California/San+Francisco"
        )
        self.assertEqual(p1.place_type, "locality")
        self.assertEqual(p1.photo_count, "156")
        self.assertEqual(p1.name, "San Francisco, California")

        # Verify pagination info
        self.assertEqual(places.info.total, 1)

    @patch.object(method_call.requests, "post")
    def test_place_places_for_user(self, mock_post):
        """Test Place.placesForUser (flickr.places.placesForUser)"""
        api_doc = load_api_doc("flickr.places.placesForUser")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        places = f.Place.placesForUser(place_type_id=7)

        # Verify we got 1 place
        self.assertEqual(len(places), 1)

        # San Francisco
        p1 = places[0]
        self.assertIsInstance(p1, f.Place)
        self.assertEqual(p1.id, "kH8dLOubBZRvX_YZ")
        self.assertEqual(p1.woeid, "2487956")
        self.assertEqual(p1.latitude, 37.779)
        self.assertEqual(p1.longitude, -122.420)
        self.assertEqual(
            p1.place_url,
            "/United+States/California/San+Francisco"
        )
        self.assertEqual(p1.place_type, "locality")
        self.assertEqual(p1.photo_count, "156")
        self.assertEqual(p1.name, "San Francisco, California")

        # Verify pagination info
        self.assertEqual(places.info.total, 1)

    @patch.object(method_call.requests, "post")
    def test_place_tags_for_place_static(self, mock_post):
        """Test Place.tagsForPlace static method (flickr.places.tagsForPlace)"""
        api_doc = load_api_doc("flickr.places.tagsForPlace")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        tags = f.Place.tagsForPlace(place_id="4hLQygSaBJ92")

        # Verify we got 12 tags in the example response
        self.assertEqual(len(tags), 12)

        # First tag - montreal
        t1 = tags[0]
        self.assertIsInstance(t1, f.Place.Tag)
        self.assertEqual(t1.text, "montreal")
        self.assertEqual(t1.count, 31775)

        # Second tag - canada
        t2 = tags[1]
        self.assertEqual(t2.text, "canada")
        self.assertEqual(t2.count, 20585)

        # Third tag - montréal (with accent)
        t3 = tags[2]
        self.assertEqual(t3.text, "montréal")
        self.assertEqual(t3.count, 12319)

        # Last tag - festival
        t12 = tags[11]
        self.assertEqual(t12.text, "festival")
        self.assertEqual(t12.count, 1419)

    @patch.object(method_call.requests, "post")
    def test_place_get_tags_instance(self, mock_post):
        """Test Place.getTags instance method (flickr.places.tagsForPlace)"""
        api_doc = load_api_doc("flickr.places.tagsForPlace")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        # Montreal place
        place = f.Place(id="4hLQygSaBJ92")
        tags = place.getTags()

        # Verify we got 12 tags
        self.assertEqual(len(tags), 12)

        # First tag - montreal
        t1 = tags[0]
        self.assertIsInstance(t1, f.Place.Tag)
        self.assertEqual(t1.text, "montreal")
        self.assertEqual(t1.count, 31775)

        # Second tag - canada
        t2 = tags[1]
        self.assertEqual(t2.text, "canada")
        self.assertEqual(t2.count, 20585)


if __name__ == "__main__":
    unittest.main()
