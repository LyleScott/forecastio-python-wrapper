from datetime import date, datetime

import requests
from dateutil.parser import parse as dateparse

from forecastiowrap.models import Location


class ForecastioWrapper(object):
    """A driver object to facilitate interacting with the forecastio api in a pythonic way."""

    API_URL_FMT = 'https://api.forecast.io/forecast/{}/%s,%s'

    def __init__(self, api_key):
        """Create a ForecastioWrapper object to hold the API key and caches.

        :param api_key: The developer key provided by forecastio.
        :type api_key: basestring
        """
        self.api_key = api_key
        self.api_url_prefix = self.API_URL_FMT.format(api_key)

    def _get_api_response(self, url):
        """Helper for making the HTTP(s) request to forecast.io

        :param url: The URL to request.
        :type url: basestring
        :returns: The text of the response.
        :rtype: basestring
        """
        response = requests.get(url)
        if response.status_code != 200:
            raise InvalidApiResponse(
                'The request to "{}" failed with the response {}'.format(
                    url, response.text))
        return response.text

    def get_location(self, lat, lng, units='us', exclude=None, extend=False, lang='en', time=None,
                     json_only=False):
        """Get the JSON for an API call.

        :param lat: The latitude to use for the API call.
        :type lat: float
        :param lng: The longitude to use for the API call.
        :type lng: float
        :param units: Return the API response in units other than the default Imperial units.
            us: The default. Uses miles, inches, and fahrenheit.
            si: Uses kilometers, centimeters, and celcius.
            ca: Same as si, except windSpeed is in kilometers per hour.
            uk: Same as si, except windSpeed is in miles per hour, as in the US.
                (This option is provided because adoption of SI in the UK has been inconsistent.)
            auto: Selects the relevant units automatically, based on geographic location.
        :type units: basestring
        :param exclude: Exclude data blocks from the API response. Should be a comma-delimeted list
            (without spaces) of any of the following: currently, minutely, hourly, daily, alerts,
            flags
        :type exclude: iter
        :param extend: Return hourly data for the next seven days, rather than the next two.
        :type extend: bool
        :param lang: Return text summaries in the desired language.
            bs (Bosnian)
            de (German)
            en (English, default)
            es (Spanish)
            fr (French)
            it (Italian)
            nl (Dutch)
            pl (Polish)
            pt (Portuguese)
            tet (Tetum)
            x-pig-latin (Igpay Atinlay).
            If a different language is desired, please consider contributing to
            https://github.com/darkskyapp/forecast-io-translations
        :type lang: basestring
        :param time: Epoch or [YYYY]-[MM]-[DD]T[HH]:[MM]:[SS][{+,-}[HH][MM]]
            For example, 1412528274 or 2014-10-05T16:59:39+0800
            NOTE: When using this parameter, you weather from mid-night to
            mid-night.
        :type time: int (seconds since epoch), date, datetime.
        :param json_only: If true, return the JSON only (instead of a Location object).
        :type json_only: bool
        :return: The JSON dict from the forecastio api response.
        :rtype: dict
        """
        url = self.api_url_prefix % (lat, lng)  # must be a format string.
        if time:
            if isinstance(time, datetime):
                time = datetime.strftime('%s')
            elif isinstance(time, date):
                time = date.strftime('%s')
            else:
                """
                try:
                    time = dateparse(time)
                except:
                    # It better be a string...just in case, run some sanity checks against the input.
                    raise ValueError(
                        'time must be an epoch, date, datetime, or a string in the format of '
                        '[YYYY]-[MM]-[DD]T[HH]:[MM]:[SS][{+,-}[HH][MM]]')
                """
                pass

            url += ',{}'.format(time)
        url += '?'
        if units:
            url += '&units={}'.format(units)
        if exclude:
            url += '&exclude={}'.format(','.join(exclude))
        if extend:
            url += '&extend=true'
        if lang:
            url += '&lang={}'.format(lang)

        location_json = self._get_api_response(url)

        if json_only:
            return location_json

        return Location.from_json(location_json)

    def get_locations(self, latlngs, units='us', exclude=None, extend=False, lang='en', time=None,
                      json_only=False):
        """Serialize lat/lng pairs into Location models.

        :param latlngs: An iterable of lat/lng pairs (ie, (lat, lng) to resolve
            into Location models.
        :type latlngs: tuple of (int, int) pairs
        :param units: Return the API response in units other than the default Imperial units.
            us: The default. Uses miles, inches, and fahrenheit.
            si: Uses kilometers, centimeters, and celcius.
            ca: Same as si, except windSpeed is in kilometers per hour.
            uk: Same as si, except windSpeed is in miles per hour, as in the US.
                (This option is provided because adoption of SI in the UK has been inconsistent.)
            auto: Selects the relevant units automatically, based on geographic location.
        :type units: basestring
        :param exclude: Exclude data blocks from the API response. Should be a comma-delimeted list
            (without spaces) of any of the following: currently, minutely, hourly, daily, alerts,
            flags
        :type exclude: iter
        :param extend: Return hourly data for the next seven days, rather than the next two.
        :type extend: bool
        :param lang: Return text summaries in the desired language.
            bs (Bosnian)
            de (German)
            en (English, default)
            es (Spanish)
            fr (French)
            it (Italian)
            nl (Dutch)
            pl (Polish)
            pt (Portuguese)
            tet (Tetum)
            x-pig-latin (Igpay Atinlay).
            If a different language is desired, please consider contributing to
            https://github.com/darkskyapp/forecast-io-translations
        :type lang: basestring
        :param time: Epoch or [YYYY]-[MM]-[DD]T[HH]:[MM]:[SS][{+,-}[HH][MM]]
            For example, 1412528274 or 2014-10-05T16:59:39+0800
            NOTE: When using this parameter, you weather from mid-night to
            mid-night.
        :type time: int (seconds since epoch), date, datetime.
        :param json_only: If true, return the JSON only (instead of a Location object).
        :type json_only: bool
        :returns: A generator of Location models.
        :rtype: generator
        """
        if not hasattr(latlngs, '__iter__'):
            raise Exception('get_locations requires latlngs to be an iterable.')
        for lat, lng in latlngs:
            yield self.get_location(
                lat, lng, units=units, exclude=exclude, extend=extend, lang=lang, time=time,
                json_only=json_only)


class InvalidApiResponse(Exception):
    """A custom Exception used for invalid forcastio api responses."""
