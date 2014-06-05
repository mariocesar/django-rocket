from unittest import skip
from django.test.utils import override_settings
from django.test import TestCase


@override_settings(DEBUG=True)
class DjangoRocketIntegrationTestCase(TestCase):
    urls = 'tests.urls'

    @skip('maybe moving integration tests to the example project')
    def test_anonymous_visit(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)