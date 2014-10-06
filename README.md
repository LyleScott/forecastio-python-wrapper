forecastio-python-wrapper
=========================

A Python wrapper for the [forcastio API service](https://forecast.io).

THIS LIBRARY STILL IN DEVELOPMENT. I am in the middle of writing tests for the
API and will be refactoring [TideNugget.com](http://tidenugget.com) to use it.
Until this, I can only guarantee that it _should_ work.


Goal
----

Create a simple API that follows the
[forecast.io development docs nomenclature](https://developer.forecast.io).
I don't really plan to do anything fancy, but I do want to make sure this
API is super simple, straightforward, and performant.


Getting Started
---------------

Create a ForecastioWrapper instance and supply it with your API key.

> If you don't have an API key, get a free one from the
> [forecastio developer portal](https://developer.forecast.io/).

```python
from forecastiowrap import ForecastioWrapper

API_KEY = 'fba3b9ccabb3c66e29a4f18e7502d126'

forecastio = ForecastioWrapper(API_KEY)
```

After you create a ForecastioWrapper instance, you have a controller for making
requests to the forecastio restful API and serializing the forecastio JSON
responses into pythonic models.

```python
# 27.7731 N, 82.6400 W   (Saint Petersburg, Florida, USA)
location = forecastio.get_location(27.7731, 82.6400)

current_temp = location.currently.temperature
feels_temp = location.currently.apparentTemperature

daily_forecast = location.daily     # 7 day forecast
hourly_forecast = location.hourly   # next 49 hours if weather
```

Read below for more in-depth documention on how the JSON responses are modeled.

The Location Model
------------------

### Holds lists of weather items.
* currently
* minutely
* hourly
* daily
* alerts
* flags

### Location attributes.
* latitude
* longitude
* offset
* timezone

### Utility method to create a Location from a forecastio JSON response.
* from_json


Contact
-------

Feel free to reach out to me directly at
[lyle@digitalfoo.net](mailto:lyle@digitalfoo.net) or use the GitHub tools if
you run into a bug, have a problem, want to suggest a feature, etc.
