

class Alerts(object):

    def __init__(self, alerts=None):
        self.alerts = [Alert.from_json(alert) for alert in alerts]

    @classmethod
    def from_json(cls, data):
        return cls(data)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '<%s count=%s %s>' % (self.__class__.__name__, len(self.alerts), id(self))

    def __getitem__(self, index):
        return self.alerts[index]


class Alert(object):
    """
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

    def __init__(self, description=None, expires=None, time=None, title=None,
                 uri=None):
        self.description = description
        self.expires = expires
        self.time = time
        self.title = title
        self.uri = uri

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