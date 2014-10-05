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


Example
-------

```python

from forecastiowrap import ForecastioWrapper

API_KEY = 'fba3b9ccabb3c66e29a4f18e7502d126'

forecastio = ForecastioWrapper(API_KEY)
# 27.7731 N, 82.6400 W   (Saint Petersburg, Florida, USA)
location = forecastio.get_location(27.7731, 82.6400)

```


Contact
-------

Feel free to reach out to me directly at
[lyle@digitalfoo.net](mailto:lyle@digitalfoo.net) or use the GitHub tools if
you run into a bug, have a problem, want to suggest a feature, etc.
