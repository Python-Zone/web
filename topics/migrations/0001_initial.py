# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uniqueid', models.CharField(unique=True, max_length=100, verbose_name=b'url\xe7\x9a\x84md5\xe5\x80\xbc')),
                ('url', models.CharField(max_length=500, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\x9a\x84url')),
                ('site', models.CharField(max_length=200, verbose_name=b'\xe6\x9d\xa5\xe6\xba\x90\xe7\xbd\x91\xe7\xab\x99')),
                ('originid', models.CharField(max_length=200, verbose_name=b'\xe6\x9d\xa5\xe6\xba\x90id')),
                ('avatar', models.CharField(max_length=500, verbose_name=b'\xe7\xbc\xa9\xe7\x95\xa5\xe5\x9b\xbe\xe5\x9c\xb0\xe5\x9d\x80')),
                ('title', models.CharField(max_length=200, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('author', models.CharField(max_length=50, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('abstract', models.TextField(default=b'', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\xae\x80\xe4\xbb\x8b')),
                ('content', models.TextField(default=b'', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x86\x85\xe5\xae\xb9')),
                ('tags', models.CharField(default=b'', max_length=50, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xa0\x87\xe7\xad\xbe,\xe4\xbb\xa5|\xe5\x88\x86\xe5\x89\xb2')),
                ('publish_time', models.DateTimeField(verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x8a\x93\xe5\x8f\x96\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
    ]
