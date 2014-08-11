
class Location(object):
    """A model to serialize an API request to a Python object.

    See https://developer.forecast.io/docs/v2 for more info.

    Example JSON:
    {
        u'alerts': [{...},],
        u'currently': {...},
        u'daily': {
            u'data': [{...},],
            u'icon': u'...',
            u'summary': u'...',
        },
        u'flags': {...},
        u'hourly': {
            u'data': [{...},],
            u'icon': u'...',
            u'summary': u'...',
        },
        u'latitude': 12.34,
        u'longitude': 45.67,
        u'minutely': {
            u'data': [{...},],
            u'icon': u'...',
            u'summary': u'...',
        },
        u'offset': -7,
        u'timezone': u'America/Los_Angeles'
    }
    """
    latitude = None
    longitude = None
    timezone = None
    offset = None
    currently = None
    minutely = None
    hourly = None
    daily = None
    alerts = None
    flags = None

    def __init__(self, latitude=None, longitude=None, timezone=None,
                 offset=None, currently=None, minutely=None, hourly=None,
                 daily=None, alerts=None, flags=None):
        """
        See https://developer.forecast.io/docs/v2 for parameter definitions.
        """
        self.latitude = latitude
        self.longitude = longitude
        self.timezone = timezone
        self.offset = offset

        from . import Currently
        self.currently = Currently.from_json(currently)

        from . import Minutes
        self.minutely = Minutes.from_json(minutely)

        from . import Hours
        self.hourly = Hours.from_json(hourly)

        from . import Days
        self.daily = Days.from_json(daily)

        from . import Alerts
        self.alerts = Alerts.from_json(alerts)

        from . import Flags
        self.flags = Flags.from_json(flags)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '<%s lat=%s lng=%s %s>' % (
            self.__class__.__name__, self.latitude, self.longitude, id(self))

    @classmethod
    def from_json(cls, data):
        """Deserialize the JSON data into a model instance.

        :param data: The JSON data to deserialize.
        :return: The model instance built from the JSON data.
        """
        return cls(**data)


