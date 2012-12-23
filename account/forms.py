# coding: utf-8
from django.forms import ModelForm
from django.forms import Textarea
from account.models import Account


class AccountEditForm(ModelForm):
    class Meta:
        model = Account
        fields = (
            "first_name", "last_name",
            "email", "jabber",
            "dob",
            "bio",
        )
        widgets = {
            'bio': Textarea(attrs={'cols': 24, 'rows': 6}),
        }
