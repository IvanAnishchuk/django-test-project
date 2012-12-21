# coding: utf-8
"""
Adds settings specified in settings.EXPOSE_SETTINGS to context.
"""
from django.conf import settings


def exposed_settings(request):
    """ Adds settings to context."""
    if (
        not hasattr(settings, 'EXPOSED_SETTINGS')
        or django_settings.EXPOSED_SETTINGS == '*'
    ):
        return {'settings': settings}
    else:
        exposed_settings = {}
        for var in django_settings.EXPOSED_SETTINGS:
            try:
                exposed_settings[var] = gettattr(settings, var)
            except AttributeError:
                pass
        return {'settings': exposed_settings}
