from tests import JsonFixture
from forecastiowrap.models.minutely import Minutes


class TestMinutes(JsonFixture):

    def setUp(self):
        super(TestMinutes, self).setUp()
        self.minutely_json = self.json_fixture['minutely'].copy()

    def test_from_json(self):
        minutes = Minutes.from_json(self.minutely_json)
        self.assertTrue(isinstance(minutes, Minutes))
        self.assertEqual(len(minutes), 61)
        self.assertEqual(minutes[0].precipIntensity, 0)
        self.assertEqual(minutes[0].precipProbability, 0)
        self.assertEqual(minutes[0].time, 1407792240)
        self.assertEqual(minutes.icon, 'clear-day')
        self.assertEqual(minutes.summary, 'Clear for the hour.')