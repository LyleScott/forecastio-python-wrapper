import unittest

from src import constants_example as constants


class ConstantsTest(unittest.TestCase):

    def test_api_url_fmt(self):
        self.assertEqual(
            constants.API_URL_FMT,
            'https://api.forecast.io/forecast/abcd1234/%s,%s')
        self.assertEqual(
            constants.API_URL_FMT % (12.34, 56.78),
            'https://api.forecast.io/forecast/abcd1234/12.34,56.78')