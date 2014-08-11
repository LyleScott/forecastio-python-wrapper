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


def get_json(lat, lng):
    """Get the JSON for an API call.

    :param lat: The latitude to use for the API call.
    :param lng: The longitude to use for the API call.
    :return: The API response for the lat/lng combo.
    """
    url = API_URL_FMT % (lat, lng)
    req = requests.get(url)
    location_json = req.json()
    return location_json


def get_location(lat, lng):
    """Get the Location object for the lat/lng pair.

    :param lat: The latitude to use for the API call.
    :param lng: The longitude to use for the API call.
    :returns: The Location model populated with the API response for the
              lat/lng combo.
    """
    location_json = get_json(lat, lng)
    return Location.from_json(location_json)


def get_locations(latlngs):
    """Serialize lat/lng pairs into Location models.

    :param latlngs: An iterable of lat/lng pairs (ie, (lat, lng) to resolve
                    into Location models.
    :returns: A generator of Location models.
    """
    for lat, lng in latlngs:
        yield get_location(lat, lng)


