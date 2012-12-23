# coding: utf-8
from django.forms import ModelForm
from django.forms import Textarea
from account.models import Account
from django.contrib.admin.widgets import AdminDateWidget


class AccountEditForm(ModelForm):
    class Meta:
        model = Account
        fields = (
            "bio",
            "dob",
            "email", "jabber",
            "last_name", "first_name",
        )
        widgets = {
            'bio': Textarea(attrs={'cols': 24, 'rows': 6}),
            'dob': AdminDateWidget()
        }
