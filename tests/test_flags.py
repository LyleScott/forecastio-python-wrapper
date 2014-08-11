from tests import JsonFixture
from src.models import Flags


class TestFlags(JsonFixture):

    def setUp(self):
        super(TestFlags, self).setUp()
        self.flags = self.json_fixture['flags'].copy()

    def test__dash_to_underscore(self):
        """Assert that dictionary keys get their dashes replaces with
        underscores.
        """
        Flags._dash_to_underscore(self.flags)
        for key in self.flags:
            self.assertNotIn('-', key)

    def test_from_json(self):
        """Assert that from_json replaces dashes in the keys and can serialze
        the passed data to a Flags instance.
        """
        flags_instance = Flags.from_json(self.flags)
        self.assertTrue(isinstance(flags_instance, Flags))
        self.assertEquals(flags_instance.darksky_stations, [
            'KMUX',
            'KDAX'])
        self.assertEquals(flags_instance.isd_stations, [
            '724943-99999',
            '745039-99999',
            '745065-99999',
            '994016-99999',
            '999999-23272'])
        self.assertEquals(flags_instance.lamp_stations, [
            'KAPC',
            'KCCR',
            'KHWD',
            'KLVK',
            'KNUQ',
            'KOAK',
            'KPAO',
            'KSFO',
            'KSQL'])
        self.assertEquals(flags_instance.madis_stations, [
            'AU915',
            'C5988',
            'C6328',
            'C8158',
            'D5422',
            'D8008',
            'D8568',
            'D8582',
            'E0426',
            'E1927',
            'FTPC1',
            'GGBC1',
            'OKXC1',
            'OMHC1',
            'PXOC1',
            'SFOC1'])
        self.assertEquals(flags_instance.sources, [
            'nwspa',
            'isd',
            'nearest-precip',
            'fnmoc',
            'sref',
            'rtma',
            'rap',
            'nam',
            'cmc',
            'gfs',
            'madis',
            'lamp',
            'darksky'])
        self.assertEquals(flags_instance.units, 'us')