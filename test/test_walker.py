import unittest
from unittest.mock import MagicMock

import flickr_api as f


class MockInfo:
    """Mock for FlickrList.info"""
    def __init__(self, pages, total):
        self.pages = pages
        self.total = total


class TestWalker(unittest.TestCase):
    def test_normal_pagination(self):
        """Test that Walker iterates through multiple pages correctly."""
        page1 = ["item1", "item2"]
        page2 = ["item3", "item4"]

        call_count = [0]

        def mock_method(**kwargs):
            call_count[0] += 1
            if call_count[0] == 1:
                result = f.objects.FlickrList(page1)
                result.info = MockInfo(pages=2, total=4)
            else:
                result = f.objects.FlickrList(page2)
                result.info = MockInfo(pages=2, total=4)
            return result

        walker = f.objects.Walker(mock_method)
        items = list(walker)

        self.assertEqual(["item1", "item2", "item3", "item4"], items)
        self.assertEqual(2, call_count[0])

    def test_empty_page_mid_pagination(self):
        """Test that empty pages in the middle are skipped (Issue #100)."""
        page1 = ["item1", "item2"]
        page2 = []  # Empty page
        page3 = ["item3", "item4"]

        call_count = [0]

        def mock_method(**kwargs):
            call_count[0] += 1
            if call_count[0] == 1:
                result = f.objects.FlickrList(page1)
                result.info = MockInfo(pages=3, total=4)
            elif call_count[0] == 2:
                result = f.objects.FlickrList(page2)
                result.info = MockInfo(pages=3, total=4)
            else:
                result = f.objects.FlickrList(page3)
                result.info = MockInfo(pages=3, total=4)
            return result

        walker = f.objects.Walker(mock_method)
        items = list(walker)

        self.assertEqual(["item1", "item2", "item3", "item4"], items)
        self.assertEqual(3, call_count[0])

    def test_multiple_consecutive_empty_pages(self):
        """Test that multiple consecutive empty pages are skipped."""
        page1 = ["item1"]
        page2 = []  # Empty page
        page3 = []  # Another empty page
        page4 = ["item2"]

        call_count = [0]

        def mock_method(**kwargs):
            call_count[0] += 1
            if call_count[0] == 1:
                result = f.objects.FlickrList(page1)
                result.info = MockInfo(pages=4, total=2)
            elif call_count[0] == 2:
                result = f.objects.FlickrList(page2)
                result.info = MockInfo(pages=4, total=2)
            elif call_count[0] == 3:
                result = f.objects.FlickrList(page3)
                result.info = MockInfo(pages=4, total=2)
            else:
                result = f.objects.FlickrList(page4)
                result.info = MockInfo(pages=4, total=2)
            return result

        walker = f.objects.Walker(mock_method)
        items = list(walker)

        self.assertEqual(["item1", "item2"], items)
        self.assertEqual(4, call_count[0])

    def test_empty_first_page(self):
        """Test that empty first page is handled correctly."""
        page1 = []  # Empty first page
        page2 = ["item1", "item2"]

        call_count = [0]

        def mock_method(**kwargs):
            call_count[0] += 1
            if call_count[0] == 1:
                result = f.objects.FlickrList(page1)
                result.info = MockInfo(pages=2, total=2)
            else:
                result = f.objects.FlickrList(page2)
                result.info = MockInfo(pages=2, total=2)
            return result

        walker = f.objects.Walker(mock_method)
        items = list(walker)

        self.assertEqual(["item1", "item2"], items)
        self.assertEqual(2, call_count[0])

    def test_all_empty_pages(self):
        """Test that iteration stops when all pages are empty."""
        def mock_method(**kwargs):
            result = f.objects.FlickrList([])
            result.info = MockInfo(pages=1, total=0)
            return result

        walker = f.objects.Walker(mock_method)
        items = list(walker)

        self.assertEqual([], items)

    def test_single_page(self):
        """Test iteration with a single page."""
        def mock_method(**kwargs):
            result = f.objects.FlickrList(["item1", "item2", "item3"])
            result.info = MockInfo(pages=1, total=3)
            return result

        walker = f.objects.Walker(mock_method)
        items = list(walker)

        self.assertEqual(["item1", "item2", "item3"], items)
