"""
Settings context processor tests
"""

from django.test import TestCase

from django.template import RequestContext
from django.test.client import RequestFactory
from django.conf import settings
from settings_context_processor.context_processors import exposed_settings


class SettingsTest(TestCase):
    """
    Test settings availability in context.
    """

    def test_exposed_settings(self):
        factory = RequestFactory()
        request = factory.get('/')
        ctx = RequestContext(request, {}, [exposed_settings])
        self.assertIn('settings', ctx)
