# coding: utf-8
from django import template
from django.core.urlresolvers import reverse, NoReverseMatch

register = template.Library()


@register.simple_tag()
def show_change_url(obj):
    try:
        url = reverse(
            (
                'admin:'
                '{obj._meta.app_label}_'
                '{obj._meta.module_name}_'
                'change'
            ).format(obj=obj),
            args=(obj.id,),
        )
    except NoReverseMatch:
        return ''
    return url
