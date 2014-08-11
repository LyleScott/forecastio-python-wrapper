'''
fba3b9ccabb3c66e29a4f18e7502d126
https://api.forecast.io/forecast/fba3b9ccabb3c66e29a4f18e7502d126/37.8267,-122.423
'''

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
    url = API_URL_FMT % (lat, lng)
    r = requests.get(url)
    return r.json()


def get_location(lat, lng):
    json = get_json(37.8267, -122.423)
    return Location.from_json(json)


def get_locations(latlngs):
    for lat, lng in latlngs:
        yield get_location(lat, lng)
