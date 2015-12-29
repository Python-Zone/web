# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.job_list, name="jobs.job_list"),
    url(r'^job/\d+/$', views.job, name="jobs.job"),

]
