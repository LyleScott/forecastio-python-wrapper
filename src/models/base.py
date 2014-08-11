

class JsonBase(object):
    """
    {
        u'precipIntensity': 0.0044,
        u'precipIntensityError': 0.0024,
        u'precipProbability': 0.01,
        u'precipType': u'rain',
        u'time': 1407722580
    }
    """

    @classmethod
    def from_json(cls, data):
        """Deserialize the JSON data into a model instance.

        :param data: The JSON data to serialize.
        :return: The model instance built from the JSON data.
        """
        return cls(**data)

    def __repr__(self):
        return '<%s time=%s %s>' % (
            self.__class__.__name__, self.time, id(self))

    def __str__(self):
        return self.__repr__()


class JsonContainer(object):
    """
    {
        'data': [
            {
                u'precipIntensity': 0.0044,
                u'precipIntensityError': 0.0024,
                u'precipProbability': 0.01,
                u'precipType': u'rain',
                u'time': 1407722580
            },
        ],
        u'icon': u'partly-cloudy-day',
        u'summary': u'Partly cloudy for the hour.'
    }
    """
    child_model = None
    icon = None
    summary = None
    hours = None

    def __init__(self, data=None, icon=None, summary=None):
        self.items = [self.child_model.from_json(item) for item in (data or [])]

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '<%s count=%s %s>' % (
            self.__class__.__name__, len(self.items), id(self))

    def __getitem__(self, index):
        return self.items[index]

    @classmethod
    def from_json(cls, data):
        """Deserialize the JSON data into a model instance.

        :param data: The JSON data to deserialize.
        :return: The model instance built from the JSON data.
        """
        return cls(**data)