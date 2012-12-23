# coding: utf-8
from django_webtest import WebTest
from django_any import any_model
from django.core.urlresolvers import reverse
from django.contrib.auth.hashers import make_password
from account.models import Account


class AccountWebTest(WebTest):

    def _create_account(self):
        acc = any_model(
            Account,
            user__is_active=True,
            user__password=make_password('qwerty'))
        return acc

    def _login(self, login, password):
        page = self.app.get(reverse('login'))
        login_form = page.forms['id_login_form']
        login_form['username'] = login
        login_form['password'] = password
        page = login_form.submit().follow()
        return page

    def test_login(self):
        acc = self._create_account()
        page = self._login(acc.user.username, 'qwerty')
        self.assertIn('<dt>Email</dt>', page)

    def test_edit_validation(self):
        acc = self._create_account()
        self._login(acc.user.username, 'qwerty')
        page = self.app.get(reverse('account_edit_profile'))
        form = page.forms['id_edit_form']
        form['jabber'] = 'user%test.com'
        page = form.submit()
        self.assertIn('error', page)

    def test_edit_save(self):
        acc = self._create_account()
        self._login(acc.user.username, 'qwerty')
        page = self.app.get(reverse('account_edit_profile'))
        form = page.forms['id_edit_form']
        form['jabber'] = 'user@test.com'
        page = form.submit()
        self.assertNotIn('error', page)
        acc = Account.objects.get(id=acc.id)
        self.assertEqual(acc.jabber, 'user@test.com')
