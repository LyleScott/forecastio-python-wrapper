from datetime import datetime

from . import DataBlock
from . import JsonBase


class Day(JsonBase):
    """
    See https://developer.forecast.io/docs/v2 for more info.

    Example JSON:
    {
        u'apparentTemperatureMax': 64.08,
        u'apparentTemperatureMaxTime': 1407715200,
        u'apparentTemperatureMin': 55.83,
        u'apparentTemperatureMinTime': 1407650400,
        u'cloudCover': 0.6,
        u'dewPoint': 53.85,
        u'humidity': 0.83,
        u'icon': u'partly-cloudy-day',
        u'moonPhase': 0.49,
        u'ozone': 327.84,
        u'precipIntensity': 0.0007,
        u'precipIntensityMax': 0.0018,
        u'precipIntensityMaxTime': 1407661200,
        u'precipProbability': 0.15,
        u'precipType': u'rain',
        u'pressure': 1014.63,
        u'summary': u'Partly cloudy throughout the day.',
        u'sunriseTime': 1407676935,
        u'sunsetTime': 1407726630,
        u'temperatureMax': 64.08,
        u'temperatureMaxTime': 1407715200,
        u'temperatureMin': 55.83,
        u'temperatureMinTime': 1407650400,
        u'time': 1407654000,
        u'visibility': 9.15,
        u'windBearing': 245,
        u'windSpeed': 6.48
    }
    """

    def __init__(self, apparentTemperatureMax=None,
                 apparentTemperatureMaxTime=None, apparentTemperatureMin=None,
                 apparentTemperatureMinTime=None, cloudCover=None,
                 dewPoint=None, humidity=None, icon=None, moonPhase=None,
                 ozone=None, precipIntensity=None, precipIntensityMax=None,
                 precipIntensityMaxTime=None, precipProbability=None,
                 precipType=None, pressure=None, summary=None,
                 sunriseTime=None, sunsetTime=None, temperatureMax=None,
                 temperatureMaxTime=None, temperatureMin=None,
                 temperatureMinTime=None, time=None, visibility=None,
                 windBearing=None, windSpeed=None):
        """See https://developer.forecast.io/docs/v2 for parameter definitions.
        """
        self.apparentTemperatureMax = apparentTemperatureMax
        self.apparentTemperatureMaxTime = apparentTemperatureMaxTime
        self.apparentTemperatureMin = apparentTemperatureMin
        self.apparentTemperatureMinTime = apparentTemperatureMinTime
        self.cloudCover = cloudCover
        self.dewPoint = dewPoint
        self.humidity = humidity
        self.icon = icon
        self.moonPhase = moonPhase
        self.ozone = ozone
        self.precipIntensity = precipIntensity
        self.precipIntensityMax = precipIntensityMax
        self.precipIntensityMaxTime = precipIntensityMaxTime
        self.precipProbability = precipProbability
        self.precipType = precipType
        self.pressure = pressure
        self.summary = summary
        self.sunriseTime = sunriseTime
        self.sunsetTime = sunsetTime
        self.temperatureMax = temperatureMax
        self.temperatureMaxTime = temperatureMaxTime
        self.temperatureMin = temperatureMin
        self.temperatureMinTime = temperatureMinTime
        self.time = time
        self.time_ = datetime.fromtimestamp(time)
        self.visibility = visibility
        self.windBearing = windBearing
        self.windSpeed = windSpeed


class Days(DataBlock):
    """A container to hold day models."""
    model = Day