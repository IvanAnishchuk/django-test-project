# coding: utf-8
""" Miscellaneous logging utils """
import logging
from django.conf import settings


class RequireDebugTrue(logging.Filter):
    """ Require debug false filter, just like in Django 1.5 """
    def filter(self, record):
        return settings.DEBUG

