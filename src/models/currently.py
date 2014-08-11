from . import Hour


class Currently(Hour):
    """
    See https://developer.forecast.io/docs/v2 for more info.

    Example JSON:
    {
        u'apparentTemperature': 62.82,
         u'cloudCover': 0.44,
         u'dewPoint': 54.53,
         u'humidity': 0.74,
         u'icon': u'partly-cloudy-day',
         u'nearestStormBearing': 73,
         u'nearestStormDistance': 24,
         u'ozone': 325.42,
         u'precipIntensity': 0,
         u'precipProbability': 0,
         u'pressure': 1013.86,
         u'summary': u'Partly Cloudy',
         u'temperature': 62.82,
         u'time': 1407718980,
         u'visibility': 9.14,
         u'windBearing': 250,
         u'windSpeed': 7.98
     }
    """
    pass