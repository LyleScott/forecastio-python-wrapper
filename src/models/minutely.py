from models import JsonBase
from models import JsonContainer


class Minute(JsonBase):
    """
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
        self.precipIntensity = precipIntensity
        self.precipIntensityError = precipIntensityError
        self.precipProbability = precipProbability
        self.precipType = precipType
        self.time = time


class Minutes(JsonContainer):
    """
    """
    child_model = Minute