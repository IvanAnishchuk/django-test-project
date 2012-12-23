# coding: utf-8
from django.test import TestCase
from django_any import any_model
from django.core.urlresolvers import reverse
from django.contrib.auth.hashers import make_password
from account.models import Account
from django.template import Template, Context


class ChangeUrlTest(TestCase):

    def _create_account(self):
        acc = any_model(
            Account,
            user__is_active=True,
            user__password=make_password('qwerty'),
        )
        return acc

    def test_admin_edit_url(self):
        acc = self._create_account()
        c = Context({'obj': acc})
        t = Template('{% load change_any_object %}{% show_change_url obj %}')
        self.assertEqual(
            t.render(c),
            reverse('admin:account_account_change', args=(acc.id, )),
        )
