from . import RelationshipContainer


class Alert(object):
    """
    An alert object represents a severe weather warning issued for the requested
    location by a governmental authority (for a list of which authorities we
    currently support, please see data sources).

    See https://developer.forecast.io/docs/v2 for more info.

    Example JSON:
    {
        u'description': u'...ISOLATED TO SCATTERED THUNDERSTORMS\n',
        u'expires': 1407866400,
        u'time': 1407701460,
        u'title': u'Fire Weather Watch for Contra Costa, CA',
        u'uri': u'http://alerts.weather.gov/cap/wwacapget.php?x=CA1D6680C.FireWeatherWatch.1249..'
    }
    """
    expires = None
    time = None
    title = None
    uri = None

    def __init__(self, title=None, expires=None, description=None, uri=None,
                 time=None):
        """
        See https://developer.forecast.io/docs/v2 for parameter definitions.
        """
        self.title = title
        self.expires = expires
        self.description = description
        self.uri = uri
        self.time = time

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '<%s title="%s" time=%s %s>' % (
            self.__class__.__name__, self.title, self.time, id(self))

    @classmethod
    def from_json(cls, data):
        """Deserialize the JSON data into a model instance.

        :param data: The JSON data to deserialize.
        :return: The model instance built from the JSON data.
        """
        return cls(**data)


class Alerts(RelationshipContainer):

    def __init__(self, alerts=None):
        super(Alerts, self).__init__(Alert, alerts)