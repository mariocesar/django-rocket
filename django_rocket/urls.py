# coding: utf-8

from __future__ import unicode_literals

from django.conf.urls import include, patterns, url
from django.contrib import admin
from .views import RequestInvitationView, RequestInvitationCompletedView, RequestAccessCompletedView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', RequestInvitationView.as_view(),
        name='request_invitation'),
    url(r'^invitation_completed/$',
        RequestInvitationCompletedView.as_view(),
        name='request_invitation_completed'),
    url(r'^request_access/$',
        RequestAccessCompletedView.as_view(),
        name='request_access')
)