from tests import JsonFixture
from forecastiowrap.models import Location


class TestLocation(JsonFixture):

    def test_from_json(self):
        """Assert that a Location instance can be deserialized from of JSON."""
        location_instance = Location.from_json(self.json_fixture)
        self.assertTrue(isinstance(location_instance, Location))
        for attr in ('alerts', 'currently', 'daily', 'flags', 'hourly',
                     'latitude', 'longitude', 'minutely', 'offset',
                     'timezone'):
            self.assertTrue(hasattr(location_instance, attr))
            self.assertTrue(getattr(location_instance, attr) is not None)

        self.assertEqual(location_instance.offset, -7)
        self.assertEqual(location_instance.timezone, 'America/Los_Angeles')