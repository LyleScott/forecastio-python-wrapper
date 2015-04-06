forecastio-python-wrapper
=========================

A Python wrapper for the [forcastio API service](https://forecast.io).

The purpose is to facilitate simple querying of weather data via a pythonic interface and to
provide serialization of responses into pythonic models.

NOTE: This library is still in some development flux as I use it more and fill in the
gaps. It is very usable, as I use it in some live projects.

Getting Started
---------------

Create a ForecastioWrapper instance and supply it with your API key.

> If you don't have an API key, get a free one from the
> [forecastio developer portal](https://developer.forecast.io/).

```python
from forecastiowrap import ForecastioWrapper

# Your key from https://developer.forecast.io
API_KEY = '123abcccabb3c66e29a4f18e7502d126'

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

The Location model
------------------

The main model is Location. It serializes a response from the forecastio 
API request to Python objects.

Attribute | Use
--------- | ----------
minutely  | contains list of minute models
hourly    | contains list of hourly models
daily     | contains a list of day models
alerts    | contains a list of alert models
flags     | contains attributes representing flags for the response
currently | contains attributes representing the current weather
latitude  | the latitude of the location for the forecast
longitude | the longitude of the location for the forecast
offset    | the timezone UTC offset
timezone  | the timezone for the request
from_json | create a Location from a forecastio JSON response

#### Weather forecast data points

Currently	|	Minute	|	Hour	|	Day
------------	|	------------	|	------------	|	------------
apparentTemperature	|		|	apparentTemperature	|	apparentTemperatureMax
 cloudCover	|		|	 cloudCover	|	 apparentTemperatureMaxTime
 dewPoint	|		|	 dewPoint	|	 apparentTemperatureMin
 from_json	|		|	 from_json	|	 apparentTemperatureMinTime
 humidity	|		|	 humidity	|	 cloudCover
 icon	|		|	 icon	|	 dewPoint
 nearestStormBearing	|		|	 nearestStormBearing	|	 from_json
 nearestStormDistance	|		|	 nearestStormDistance	|	 humidity
 ozone	|		|	 ozone	|	 icon
 precipIntensity	|		|	 precipIntensity	|	 moonPhase
 precipIntensityError	|		|	 precipIntensityError	|	 ozone
 precipProbability	|		|	 precipProbability	|	 precipIntensity
 precipType	|		|	 precipType	|	 precipIntensityMax
 pressure	|		|	 pressure	|	 precipIntensityMaxTime
 summary	|		|	 summary	|	 precipProbability
 temperature	|		|	 temperature	|	 precipType
 time	|		|	 time	|	 pressure
 time_	|		|	 time_	|	 summary
 visibility	|		|	 visibility	|	 sunriseTime
 windBearing	|		|	 windBearing	|	 sunsetTime
 windSpeed	|		|	 windSpeed	|	 temperatureMax
	|		|		|	 temperatureMaxTime
	|		|		|	 temperatureMin
	|		|		|	 temperatureMinTime
	|		|		|	 time
	|		|		|	 time_
	|		|		|	 visibility
	|		|		|	 windBearing
	|		|		|	 windSpeed
	
#### Misc data points

Alerts	|	Flags
------------	|	------------
from_json	|	darksky_stations
 items	|	 darksky_unavailable
 model	|	 datapoint_stations
	|	 from_json
	|	 isd_stations
	|	 lamp_stations
	|	 madis_stations
	|	 metar_stations
	|	 sources
	|	 units

#### Managers of lists of data points

Minutely	|	Hourly	|	Daily
------------	|	------------	|	------------
data	|	data	|	data
 from_json	|	 from_json	|	 from_json
 icon	|	 icon	|	 icon
 items	|	 items	|	 items
 model	|	 model	|	 model
 summary	|	 summary	|	 summary

Contact
-------

Feel free to reach out to me directly at
[lyle@digitalfoo.net](mailto:lyle@digitalfoo.net) or use the GitHub tools if
you run into a bug, have a problem, want to suggest a feature, etc.
