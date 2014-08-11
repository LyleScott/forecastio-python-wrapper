import gzip
import json
import os
import unittest


class JsonFixture(unittest.TestCase):
    json_fixture = None

    def setUp(self):
        self.json_fixture = self.get_json_fixture()

    def get_json_fixture(self):
        json_fixture_file = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'example',
            'example_location.json.gz'
        )
        with gzip.open(json_fixture_file) as fp:
            json_fixture = json.loads(fp.read())

        return json_fixture