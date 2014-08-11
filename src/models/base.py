
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
    time = None

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


class RelationshipContainer(object):
    """An object to manage one-to-many relationships with models."""
    model = None
    items = None

    def __init__(self, model=None, items=None):
        self.model = model
        self.items = [self.model.from_json(item) for item in (items or [])]

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '<%s count=%s %s>' % (
            self.__class__.__name__, len(self.items), id(self))

    def __getitem__(self, index):
        return self.items[index]

    def __bool__(self):
        """The Python 3.x override for the behavior of
        "if RelationshipContainerObject:" so that True is returned only if
        self.items actually contains items.
        """
        return bool(self.items)

    def __nonzero__(self):
        """The Python 2.x override for the behavior of
        "if RelationshipContainerObject:" so that True is returned only if
        self.items actually contains items.
        """
        return self.__bool__()

    @classmethod
    def from_json(cls, data):
        """Deserialize the JSON data into a model instance.

        :param data: The JSON data to deserialize.
        :return: The model instance built from the JSON data.
        """
        return cls(**data)


class DataBlock(RelationshipContainer):
    """
    A data block object represents the various weather phenomena occurring over
    a period of time.

    See https://developer.forecast.io/docs/v2 for more info.

    Example JSON:
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
    model = None
    summary = None
    icon = None
    data = None

    def __init__(self, summary=None, icon=None, data=None):
        """
        See https://developer.forecast.io/docs/v2 for parameter definitions.
        """
        super(DataBlock, self).__init__(self.model, data)
        self.summary = summary
        self.icon = icon

    def __len__(self):
        return len(self.items) if self.items else 0