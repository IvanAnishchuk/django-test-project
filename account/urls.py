# coding: utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'account.views.view_profile', name='account_view_profile'),
    # url(r'^edit/', 'account.views.edit_profile', name='account_edit_profile'),
)
