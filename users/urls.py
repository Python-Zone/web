# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^signup/$', views.signup, name="users.signup"),
    url(r'^signin/$', views.signin, name="users.signin"),
    url(r'^signout/$', views.signout, name="users.signout"),
    url(r'^(?P<name>\w+)/$', views.user_home, name="users.user_home"),
    url(r'^(?P<name>\w+)/replies/$', views.user_replies, name="users.user_replies"),
]
