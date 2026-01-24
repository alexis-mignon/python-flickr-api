import unittest

from flickr_api.method_call import clean_args


class TestCleanArgs(unittest.TestCase):
    def test_float_timestamps_converted_to_int(self):
        """Test that float timestamps are converted to int (Issue #94)."""
        args = {
            'min_upload_date': 1527638245.75,
            'max_upload_date': 1527638999.5,
            'text': 'test',
        }
        clean_args(args)

        self.assertEqual(1527638245, args['min_upload_date'])
        self.assertEqual(1527638999, args['max_upload_date'])
        self.assertEqual('test', args['text'])

    def test_all_timestamp_params_converted(self):
        """Test that all timestamp parameters are converted."""
        args = {
            'min_upload_date': 1000.1,
            'max_upload_date': 2000.2,
            'min_taken_date': 3000.3,
            'max_taken_date': 4000.4,
            'min_date': 5000.5,
            'max_date': 6000.6,
        }
        clean_args(args)

        self.assertEqual(1000, args['min_upload_date'])
        self.assertEqual(2000, args['max_upload_date'])
        self.assertEqual(3000, args['min_taken_date'])
        self.assertEqual(4000, args['max_taken_date'])
        self.assertEqual(5000, args['min_date'])
        self.assertEqual(6000, args['max_date'])

    def test_integer_timestamps_pass_through(self):
        """Test that integer timestamps are unchanged."""
        args = {
            'min_upload_date': 1527638245,
            'max_upload_date': 1527638999,
        }
        clean_args(args)

        self.assertEqual(1527638245, args['min_upload_date'])
        self.assertEqual(1527638999, args['max_upload_date'])

    def test_string_timestamps_pass_through(self):
        """Test that string timestamps (MySQL datetime format) are unchanged."""
        args = {
            'min_taken_date': '2018-05-30 12:34:56',
            'max_taken_date': '2018-05-31 23:59:59',
        }
        clean_args(args)

        self.assertEqual('2018-05-30 12:34:56', args['min_taken_date'])
        self.assertEqual('2018-05-31 23:59:59', args['max_taken_date'])

    def test_bool_conversion_still_works(self):
        """Test that bool to int conversion still works."""
        args = {
            'is_public': True,
            'is_friend': False,
        }
        clean_args(args)

        self.assertEqual(1, args['is_public'])
        self.assertEqual(0, args['is_friend'])

    def test_non_timestamp_floats_unchanged(self):
        """Test that floats in non-timestamp params are not converted."""
        args = {
            'lat': 37.7749,
            'lon': -122.4194,
        }
        clean_args(args)

        self.assertEqual(37.7749, args['lat'])
        self.assertEqual(-122.4194, args['lon'])
