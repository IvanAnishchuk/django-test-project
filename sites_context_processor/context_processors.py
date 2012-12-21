# coding: utf-8
"""
Adds site domain and name to context.
"""
from django.contrib.sites.models import get_current_site


def current_site(request):
    """ Adds site to context."""
    site = get_current_site(request)
    return {
        'SITE_NAME': site.name,
        'SITE_DOMAIN': site.domain,
    }
