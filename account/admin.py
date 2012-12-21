# coding: utf-8
""" Account admin """
from django.conf import settings
from django.contrib import admin
from django import forms
from account.models import Account


class AccountAdmin(admin.ModelAdmin):
    """ Admin class for Account model """
    list_display = ('user', 'email', 'first_name', 'last_name')
    search_fields = ('user', 'email', 'first_name', 'last_name')

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = (
            super(AccountAdmin, self)
            .formfield_for_dbfield(db_field, **kwargs)
        )
        if db_field.name == 'bio':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield


admin.site.register(Account, AccountAdmin)
