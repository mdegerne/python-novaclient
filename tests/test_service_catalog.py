import os
import mock
import httplib2

from novaclient import service_catalog
from tests import utils


SERVICE_CATALOG = {'auth': {'token': {'id': "FAKE_ID", },
                            'serviceCatalog': {
                                "nova": [{"publicURL": "http://fakeurl"}],
                                "glance": [{"publicURL": "http://fakeurl"}],
                                "swift": [{"publicURL": "http://fakeurl"}],
                                "identity": [{"publicURL": "http://fakeurl"}],
                            }}}


class ServiceCatalogTest(utils.TestCase):
    def test_building_a_service_catalog(self):
        sc = service_catalog.ServiceCatalog(SERVICE_CATALOG)

        self.assertEqual(sc.__repr__(), "<ServiceCatalog: FAKE_ID>")
        self.assertEqual(sc.token.__repr__(), "<TokenCatalog: FAKE_ID>")
        self.assertEqual(sc.nova.__repr__(), "[<NovaCatalog: http://fakeurl>]")

        self.assertEqual(sc.token.id, "FAKE_ID")
        self.assertEqual(sc.url_for('nova', 'public'),
            SERVICE_CATALOG['auth']['serviceCatalog']['nova'][0]['publicURL'])
