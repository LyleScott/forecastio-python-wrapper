# This is just a fix to put the module into PYTHONPATH
import os, sys
sys.path.insert(1, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

import json
from time import time

from api import get_json
from api import get_location
from api import get_locations


def get_request_json():
    """Get the raw JSON response from an API call."""
    json_response = get_json(37.8267, -122.423)
    print json.dumps(json_response, sort_keys=True, indent=4,
                     separators=(',', ': '))


def get_request_json_with_time():
    """Get the raw JSON response from an API call for a specific time."""
    time_ = time()
    json_response = get_json(37.8267, -122.423, time_)
    print json.dumps(json_response, sort_keys=True, indent=4,
                 separators=(',', ': '))


def get_location_object():
    """Serialize an API request to a Location object representing all elements
    of the API response (see models/location.py docstrings for more info).
    """
    location = get_location(37.8267, -122.423)
    print 'Location', location
    print 'Alerts', location.alerts
    if location.alerts:
        print 'Alert', location.alerts[0].description
    print 'Currently', location.currently.temperature


def get_multiple_locations():
    """Serialize multiple coordinated into an iterable of Location objects."""
    coords = ((34.2233, 77.9122), (27.7731, 82.6400))
    locations = get_locations(coords)
    for location in locations:
        print location.currently.temperature


if __name__ == '__main__':
    """Run different examples."""
    get_request_json()
    #get_request_json_with_time()
    #get_location_object()
    #get_multiple_locations()