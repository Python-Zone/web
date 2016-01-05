# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^signup/$', views.signup, name="users.signup"),
    url(r'^signin/$', views.signin, name="users.signin"),
    url(r'^signout/$', views.signout, name="users.signout"),
    url(r'^(?P<name>\w+)/$', views.user, name="users.user"),
]
