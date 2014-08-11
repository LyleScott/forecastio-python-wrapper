

class Location(object):

    latitude = None
    longitude = None
    offset = None
    timezone = None

    def __init__(self, latitude=None, longitude=None, offset=None, timezone=None, flags=None,
                 alerts=None, currently=None, daily=None, hourly=None, minutely=None):
        self.latitude = latitude
        self.longitude = longitude
        self.offset = offset
        self.timezone = timezone
        self.flags = flags

        from . import Alerts
        self.alerts = Alerts.from_json(alerts)

        from . import Currently
        self.currently = Currently.from_json(currently)

        from . import Days
        self.daily = Days.from_json(daily)

        from . import Hours
        self.hourly = Hours.from_json(hourly)

        from . import Minutes
        self.minutely = Minutes.from_json(minutely)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '<%s lat=%s lng=%s %s>' % (self.__class__.__name__, self.latitude, self.longitude, id(self))

    @classmethod
    def from_json(cls, data):
        return cls(**data)


