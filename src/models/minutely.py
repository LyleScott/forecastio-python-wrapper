from . import DataBlock
from . import JsonBase


class Minute(JsonBase):
    """
    See https://developer.forecast.io/docs/v2 for more info.

    Example JSON:
    {
        u'precipIntensity': 0.0044,
        u'precipIntensityError': 0.0024,
        u'precipProbability': 0.01,
        u'precipType': u'rain',
        u'time': 1407722580
    }
    """

    def __init__(self, precipIntensity=None, precipIntensityError=None,
                 precipProbability=None, precipType=None, time=None):
        """
        See https://developer.forecast.io/docs/v2 for parameter definitions.
        """
        self.precipIntensity = precipIntensity
        self.precipIntensityError = precipIntensityError
        self.precipProbability = precipProbability
        self.precipType = precipType
        self.time = time


class Minutes(DataBlock):
    """
    """
    model = Minute