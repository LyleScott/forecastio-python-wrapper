try:
    import simplejson as json
except ImportError:
    try:
        import ujson as json
    except ImportError:
        import json

import requests

from forecastiowrap.models import Location


class ForecastioWrapper(object):
    """A driver object to facilitate interacting with the forecastio api in a
    pythonic way.
    """

    API_URL_FMT = 'https://api.forecast.io/forecast/{}/%s,%s'

    def __init__(self, api_key):
        """Create a ForecastioWrapper object to hold the API key and caches.

        :param api_key: The developer key provided by forecastio.
        :type api_key: basestring
        """
        self.api_key = api_key
        self.api_url_prefix = self.API_URL_FMT.format(api_key)

    def _get_api_response(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            raise InvalidApiResponse(
                'The request to "{}" failed with the response {}'.format(
                    url, response.text))
        return response.json()

    def _exclude_keys_from_json(self, location_json, keys):
        """A helper to exclude/remove keys from the JSON response.

        :param location_json: The JSON dict to remove keys from.
        :type location_json: dict
        :param keys: The keys to remove from the JSON dict.
        :type keys: iter
        :returns: The JSON dict, minus and of the keys that were to be removed.
        :rtype: dict
        """
        for key in (keys or []):
            del location_json[key]

    def get_location_json(self, lat, lng, time=None, exclude_keys=None):
        """Get the JSON for an API call.

        :param lat: The latitude to use for the API call.
        :type lat: float
        :param lng: The longitude to use for the API call.
        :type lng: float
        :param time: Epoch or [YYYY]-[MM]-[DD]T[HH]:[MM]:[SS][{+,-}[HH][MM]]
            For example, 1412528274 or 2014-10-05T16:59:39+0800
            NOTE: When using this parameter, you weather from mid-night to
            mid-night.
        :return: The JSON dict from the forecastio api response.
        :rtype: dict
        """
        url = self.api_url_prefix % (lat, lng)
        if time:
            url = '%s,%s' % (url, time)

        location_json = self._get_api_response(url)
        self._exclude_keys_from_json(location_json, exclude_keys)

        return location_json

    def get_location(self, lat, lng, time=None, exclude_keys=None):
        """Get the Location object for the lat/lng pair.

        :param lat: The latitude to use for the API call.
        :type lat: float
        :param lng: The longitude to use for the API call.
        :type lng: float
        :param time:
        :type time:
        :param exclude_keys: The attributes to exclude from created Location.
        :param exclude_keys: None or iter
        :returns: A Location that was deserialized from a forecastio api
            response.
        :rtype: Location
        """
        location_json = self.get_location_json(
            lat, lng, time=time, exclude_keys=exclude_keys)

        return Location.from_json(location_json)

    def get_locations(self, latlngs, time=None, json_only=False,
                      exclude_keys=None):
        """Serialize lat/lng pairs into Location models.

        :param latlngs: An iterable of lat/lng pairs (ie, (lat, lng) to resolve
            into Location models.
        :type latlngs: tuple of (int, int) pairs
        :returns: A generator of Location models.
        """
        for lat, lng in latlngs:
            if json_only:
                yield self.get_location_json(
                    lat, lng, time=time, exclude_keys=exclude_keys)
            else:
                yield self.get_location(
                    lat, lng, time=time, exclude_keys=exclude_keys)


class InvalidApiResponse(Exception):
    """A custom Exception used for invalid forcastio api responses."""
