try:
    import simplejson as json
except ImportError:
    try:
        import ujson as json
    except ImportError:
        import json

import requests

from constants import API_URL_FMT
from models import Location


def get_json(lat, lng, time=None, exclude_keys=None):
    """Get the JSON for an API call.

    :param lat: The latitude to use for the API call.
    :param lng: The longitude to use for the API call.
    :param time: Should either be a UNIX time (that is, seconds since midnight
                 GMT on 1 Jan 1970) or a string formatted as follows:
                 [YYYY]-[MM]-[DD]T[HH]:[MM]:[SS] (with an optional time zone
                 formatted as Z for GMT time or {+,-}[HH][MM] for an offset in
                 minutes or seconds). For the latter format, if no timezone is
                 present, local time (at the provided latitude and longitude) is
                 assumed. (This string format is a subset of ISO 8601 time. An
                 as example, 2013-05-06T12:00:00-0400.)

                 If a time is provided in this way, only the conditions for the
                 day on which that time occurred (or will occur),
                 midnight-to-midnight, are provided; in all other ways, making
                 such a request is equivalent to getting in a time machine,
                 going back or forward in time to the given moment, and making
                 a normal forecast request. (In fact, this is how it is
                 implemented behind-the-scenes.) Generally speaking, forecasted
                 data is more accurate the nearer you query to the present
                 moment. (That is, the present moment if you don't have a time
                 machine.)
    :return: The API response for the lat/lng combo.
    """
    url = API_URL_FMT % (lat, lng)
    if time:
        url = '%s,%s' % (url, time)
    req = requests.get(url)
    location_json = req.json()
    for key in (exclude_keys or []):
        del location_json[key]

    return location_json


def get_location(lat, lng, time=None, json_only=False, exclude_keys=None):
    """Get the Location object for the lat/lng pair.

    :param lat: The latitude to use for the API call.
    :param lng: The longitude to use for the API call.
    :returns: The Location model populated with the API response for the
              lat/lng combo.
    """
    location_json = get_json(lat, lng, time=time, exclude_keys=exclude_keys)
    if json_only:
        return location_json

    return Location.from_json(location_json)


def get_locations(latlngs):
    """Serialize lat/lng pairs into Location models.

    :param latlngs: An iterable of lat/lng pairs (ie, (lat, lng) to resolve
                    into Location models.
    :returns: A generator of Location models.
    """
    for lat, lng in latlngs:
        yield get_location(lat, lng)




