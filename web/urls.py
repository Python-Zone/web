"""PythonZone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from . import views

from ckeditor_uploader import views as ck_views
from django.views.decorators.cache import never_cache
ckeditor_uploader_urlpatterns = [
        url(r'^upload/', ck_views.upload, name='ckeditor_upload'),
        url(r'^browse/', never_cache(ck_views.browse), name='ckeditor_browse'),
]
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^captcha/', include('captcha.urls')),
    url(r'^qiniu/uptoken/', views.qiniu_uptoken),
    url(r'^ckeditor/', include(ckeditor_uploader_urlpatterns)),


    url(r'^users/', include('users.urls')),
    url(r'^topics/', include('topics.urls')),
    url(r'^wiki/', include('wiki.urls')),
    url(r'^jobs/', include('jobs.urls')),
    url(r'^sites/', include('sites.urls')),
    url(r'^weixin/', include('weixin.urls')),

]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True})
    ]
