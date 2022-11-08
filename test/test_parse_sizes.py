import flickr_api as f
import unittest


class TestPhotoSizes(unittest.TestCase):
    def test_video_largest_size(self):
        p = f.objects.Photo(
            id=1234,
            sizes={
                "HD MP4":
                dict(
                    media="video",
                    url="v@url",
                    source="v@source",
                    width=100,
                    height=100,
                ),
                "Large":
                dict(
                    media="photo",
                    url="p@url",
                    source="p@source",
                    width=2000,
                    height=2000)
            },
            media="video")
        self.assertEqual("HD MP4", p._getLargestSizeLabel())

    def test_video_none_entry(self):
        p = f.objects.Photo(
            id=1234,
            sizes={
                "HD MP4":
                dict(
                    media="video",
                    url="v@url",
                    source="v@source",
                    width=100,
                    height=100,
                ),
                700:
                dict(
                    media="video",
                    url="v@url2",
                    source="v@source2",
                    width=None,
                    height=None)
            },
            media="video")
        self.assertEqual("HD MP4", p._getLargestSizeLabel())

    def test_video_output_filename(self):
        p = f.objects.Photo(
            id=1234,
            sizes={
                "HD MP4":
                dict(
                    media="video",
                    url="v@url",
                    source="v@source",
                    width=100,
                    height=100,
                )
            },
            media="video")
        self.assertEqual("source.mp4", p._getOutputFilename("source", "HD MP4"))
        self.assertEqual("source.mp4", p._getOutputFilename("source.mp4", "HD MP4"))
        self.assertEqual("source.jpeg", p._getOutputFilename("source.jpeg", "HD MP4"))

    def test_photo_output_filename(self):
        p = f.objects.Photo(
            id=1234,
            sizes={
                "Large":
                dict(
                    media="photo",
                    url="p@url",
                    source="p/source.jpg",
                    width=2000,
                    height=2000)
            },
            media="photo")
        self.assertEqual("source.jpg", p._getOutputFilename("source", "Large"))
        self.assertEqual("source.jpg", p._getOutputFilename("source.jpg", "Large"))
        self.assertEqual("source.jpeg", p._getOutputFilename("source.jpeg", "Large"))


    def test_photo_largest_size(self):
        p = f.objects.Photo(
            id=1234,
            sizes={
                "HD MP4":
                dict(
                    media="video",
                    url="v@url",
                    source="v@source",
                    width=100,
                    height=100,
                ),
                "Large":
                dict(
                    media="photo",
                    url="p@url",
                    source="p@source",
                    width=2000,
                    height=2000)
            },
            media="photo")
        self.assertEqual("Large", p._getLargestSizeLabel())

    def test_parse_inline_sizes(self):
        self.maxDiff = None
        sizes = f.objects._parse_inline_sizes({
            'title':
            'Noir comme le soleil',
            'owner':
            f.objects.Person(id="qwerty", token="abcde"),
            'id':
            16180339,
            'ispublic':
            True,
            'isfriend':
            False,
            'isfamily':
            False,
            'url_c':
            'https://farm5.staticflickr.com/X/46284324564_0a1bf6145a_c.jpg',
            'height_c':
            534,
            'width_c':
            '800',
            'url_l':
            'https://farm5.staticflickr.com/X/46284324564_0a1bf6145a_b.jpg',
            'height_l':
            '684',
            'width_l':
            '1024',
            'url_o':
            'https://farm5.staticflickr.com/X/46284324564_2baac8acd5_o.jpg',
            'height_o':
            '4016',
            'width_o':
            '6016',
            'media':
            'photo',
        })
        self.assertEqual({
            'Original': {
                'label':
                'Original',
                'width':
                '6016',
                'height':
                '4016',
                'source':
                'https://farm5.staticflickr.com/X/46284324564_2baac8acd5_o.jpg',
                'url':
                'https://www.flickr.com/photos/qwerty/16180339/sizes/o/',
                'media':
                'photo'
            },
            'Medium 800': {
                'label':
                'Medium 800',
                'width':
                '800',
                'height':
                534,
                'source':
                'https://farm5.staticflickr.com/X/46284324564_0a1bf6145a_c.jpg',
                'url':
                'https://www.flickr.com/photos/qwerty/16180339/sizes/c/',
                'media':
                'photo'
            },
            'Large': {
                'label':
                'Large',
                'width':
                '1024',
                'height':
                '684',
                'source':
                'https://farm5.staticflickr.com/X/46284324564_0a1bf6145a_b.jpg',
                'url':
                'https://www.flickr.com/photos/qwerty/16180339/sizes/l/',
                'media':
                'photo'
            },
        }, sizes)
