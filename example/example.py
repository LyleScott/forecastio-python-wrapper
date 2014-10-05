from pprint import pprint
from forecastiowrap import ForecastioWrapper

API_KEY = 'fba3b9ccabb3c66e29a4f18e7502d126'

forecastio = ForecastioWrapper(API_KEY)

# 27.7731 N, 82.6400 W  ==  Saint Petersburg, Florida, USA
location = forecastio.get_location(27.7731, 82.6400)
print(location)
print(location.hourly[0].temperature)
pprint([attr for attr in dir(location) if not attr.startswith('_')])

print(location.currently)
pprint([attr for attr in dir(location.currently) if not attr.startswith('_')])

print(location.minutely)
pprint([attr for attr in dir(location.minutely) if not attr.startswith('_')])

print(location.hourly)
pprint([attr for attr in dir(location.hourly) if not attr.startswith('_')])

print(location.daily)
pprint([attr for attr in dir(location.daily) if not attr.startswith('_')])

print(location.alerts)
pprint([attr for attr in dir(location.alerts) if not attr.startswith('_')])

print(location.flags)
pprint([attr for attr in dir(location.flags) if not attr.startswith('_')])
