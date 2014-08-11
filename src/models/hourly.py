from models import JsonBase
from models import JsonContainer


class Hour(JsonBase):
    """
    {
        u'apparentTemperature': 62.9,
        u'cloudCover': 0.45,
        u'dewPoint': 54.57,
        u'humidity': 0.74,
        u'icon': u'partly-cloudy-day',
        u'ozone': 325.42,
        u'precipIntensity': 0,
        u'precipProbability': 0,
        u'pressure': 1013.86,
        u'summary': u'Partly Cloudy',
        u'temperature': 62.9,
        u'time': 1407718800,
        u'visibility': 9.17,
        u'windBearing': 250,
        u'windSpeed': 8
    }
    """

    def __init__(self, apparentTemperature=None, cloudCover=None, dewPoint=None,
                 humidity=None, icon=None, nearestStormBearing=None,
                 nearestStormDistance=None, ozone=None, precipIntensity=None,
                 precipProbability=None, pressure=None, summary=None,
                 temperature=None, time=None, visibility=None, windBearing=None,
                 windSpeed=None):
        self.apparentTemperature = apparentTemperature
        self.cloudCover = cloudCover
        self.dewPoint = dewPoint
        self.humidity = humidity
        self.icon = icon
        self.nearestStormBearing = nearestStormBearing
        self.nearestStormDistance = nearestStormDistance
        self.ozone = ozone
        self.precipIntensity = precipIntensity
        self.precipProbability = precipProbability
        self.pressure = pressure
        self.summary = summary
        self.temperature = temperature
        self.time = time
        self.visibility = visibility
        self.windBearing = windBearing
        self.windSpeed = windSpeed


class Hours(JsonContainer):
    child_model = Hour
