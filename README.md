forecastio-wrapper
==================

A Python wrapper for the [forcastio API service](https://forecast.io).

THIS LIBRARY STILL IN DEVELOPMENT. NOT AT ALL READY FOR CONSUMPTION.


Goal
----

Create a simple API that follows the
[forecast.io development docs nomenclature](https://developer.forecast.io).
I don't really plan to do anything fancy, but I do want to make sure this
API is super simple, straightforward, and performant.


Example
-------

```python
def _pretty_json(data):
    print json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))


def get_request_json():
    """Get the raw JSON response from an API call."""
    json_response = get_json(37.8267, -122.423)
    print _pretty_json(json_response)


def get_request_json_with_time():
    """Get the raw JSON response from an API call for a specific time."""
    time_ = time()
    json_response = get_json(37.8267, -122.423, time_)
    print _pretty_json(json_response)


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
    """Serialize multiple coordinates into an iterable of Location objects."""
    coords = ((34.2233, 77.9122), (27.7731, 82.6400))
    locations = get_locations(coords)
    for location in locations:
        print location.currently.temperature
```


Contact
-------

Feel free to reach out to me directly at
[lyle@digitalfoo.net](mailto:lyle@digitalfoo.net) or use the GitHub tools if
you run into a bug, have a problem, want to suggest a feature, etc.