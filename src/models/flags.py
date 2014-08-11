
class Flags(object):
    """The flags object contains various metadata information related to the
    request.
    """
    darksky_unavailable = None
    darksky_stations = None
    datapoint_stations = None
    isd_stations = None
    lamp_stations = None
    metar_stations = None
    sources = None
    units = None

    def __init__(self, darksky_unavailable=None, darksky_stations=None,
                 datapoint_stations=None, isd_stations=None, lamp_stations=None,
                 madis_stations=None, metar_stations=None, sources=None,
                 units=None):
        """
        See https://developer.forecast.io/docs/v2 for parameter definitions.
        """
        self.darksky_unavailable = darksky_unavailable
        self.darksky_stations = darksky_stations
        self.datapoint_stations = datapoint_stations
        self.isd_stations = isd_stations
        self.lamp_stations = lamp_stations
        self.metar_stations = metar_stations
        self.madis_stations = madis_stations
        self.sources = sources
        self.units = units

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, id(self))

    @classmethod
    def from_json(cls, data):
        """Deserialize the JSON data into a model instance.

        :param data: The JSON data to deserialize.
        :return: The model instance built from the JSON data.
        """
        return cls(**data)