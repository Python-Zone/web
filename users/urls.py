# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^signup/$', views.signup, name="users.signup"),
    url(r'^signin/$', views.signin, name="users.signin"),
    url(r'^signout/$', views.signout, name="users.signout"),
    url(r'^captcha/refresh/$', views.captcha_refresh, name="users.captcha_refresh"),
    url(r'^(?P<name>\w+)/$', views.user_home, name="users.user"),
    url(r'^(?P<name>\w+)/replies/$', views.user_replies, name="users.user_replies"),
    url(r'^(?P<name>\w+)/following/$', views.user_following, name="users.user_following"),
    url(r'^(?P<name>\w+)/followers/$', views.user_followers, name="users.user_followers"),
    url(r'^(?P<name>\w+)/favorites/$', views.user_favorites, name="users.user_favorites"),

    url(r'^(?P<name>\w+)/follow/$', views.user_follow, name="users.user_follow"),
    url(r'^(?P<name>\w+)/unfollow/$', views.user_unfollow, name="users.user_unfollow"),
]
