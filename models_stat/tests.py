from django.test import TestCase
from django.core.management import call_command
from django.db.models import get_models
from django.contrib.contenttypes.models import ContentType
from StringIO import StringIO
import sys
import re


class CommandTest(TestCase):

    def test_contenttypes(self):
        outstream = StringIO()
        sys.stdout = outstream
        call_command('models_stat')
        sys.stdout = sys.__stdout__
        string = outstream.getvalue()
        self.assertIn('contenttypes.contenttype', string)
        real_count = ContentType.objects.count()
        parsed_count = int(re.search(
            '^contenttypes.contenttype (?P<count>\d+)$',
            string,
            re.MULTILINE,
        ).groupdict()['count'])
        self.assertEqual(real_count, parsed_count)

    def test_modelcount(self):
        outstream = StringIO()
        sys.stdout = outstream
        call_command('models_stat')
        sys.stdout = sys.__stdout__
        string = outstream.getvalue()
        self.assertEqual(
            len(string.splitlines()),
            len(get_models()),
        )
