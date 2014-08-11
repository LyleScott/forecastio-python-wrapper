from tests import JsonFixture
from src.models import Flags


class TestFlags(JsonFixture):

    def setUp(self):
        super(TestFlags, self).setUp()
        self.flags = self.json_fixture['flags'].copy()

    def test_dash_to_underscore(self):
        """Assert that dictionary keys get their dashes replaces with
        underscores.
        """
        Flags._dash_to_underscore(self.flags)
        for key in self.flags:
            self.assertNotIn('-', key)