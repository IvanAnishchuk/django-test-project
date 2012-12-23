# coding: utf-8
""" Action logger models """
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ActionNote(models.Model):
    class Meta:
        verbose_name = _('Action Note')
        verbose_name_plural = _('Action Notes')
    datetime = models.DateTimeField()
    note = models.CharField(max_length=64)
    app = models.CharField(max_length=64)
    model = models.CharField(max_length=32)
    object_id = models.IntegerField()
