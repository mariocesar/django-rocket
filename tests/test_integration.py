from django.test.utils import override_settings
from django.test import TestCase


@override_settings(DEBUG=True)
class DjangoBuzzIntegrationTestCase(TestCase):
    urls = 'tests.urls'

    def test_anonymous_visit(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)