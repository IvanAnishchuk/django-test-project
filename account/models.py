# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Account(models.Model):
    user = models.ForeignKey(User, unique=True)
    first_name = models.CharField(
        _('first name'),
        max_length=30,
        blank=True,
    )
    last_name = models.CharField(
        _('last name'),
        max_length=30,
        blank=True,
    )
    email = models.EmailField(
        _('e-mail address'),
        blank=True,
    )
    jabber = models.EmailField(
        _('jabber jid'),
        blank=True,
    )
    dob = models.DateField(
        _('date of birth'),
        null=True,
    )
    bio = models.CharField(
        _('bio'),
        blank=True,
        max_length=300,
    )
    def save(self):
        super(Account, self).save()
        self.user.first_name = self.first_name
        self.user.last_name = self.last_name
        self.user.email = self.email
        self.user.save()
