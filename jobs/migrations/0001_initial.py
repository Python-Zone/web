# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uniqueid', models.CharField(unique=True, max_length=100, verbose_name=b'url\xe7\x9a\x84md5\xe5\x80\xbc')),
                ('url', models.CharField(max_length=500, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\x9a\x84url')),
                ('site', models.CharField(max_length=200, verbose_name=b'\xe6\x9d\xa5\xe6\xba\x90\xe7\xbd\x91\xe7\xab\x99')),
                ('originid', models.CharField(max_length=200, verbose_name=b'\xe6\x9d\xa5\xe6\xba\x90id')),
                ('avatar', models.CharField(max_length=500, verbose_name=b'\xe7\xbc\xa9\xe7\x95\xa5\xe5\x9b\xbe\xe5\x9c\xb0\xe5\x9d\x80')),
                ('title', models.CharField(max_length=200, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('description', models.TextField(verbose_name=b'\xe8\x81\x8c\xe4\xbd\x8d\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('salary_min', models.IntegerField(default=0, verbose_name=b'\xe6\x9c\x80\xe4\xbd\x8e\xe8\x96\xaa\xe8\xb5\x84')),
                ('salary_max', models.IntegerField(default=0, verbose_name=b'\xe6\x9c\x80\xe9\xab\x98\xe8\x96\xaa\xe8\xb5\x84')),
                ('city', models.CharField(default=b'', max_length=50, verbose_name=b'\xe5\x9f\x8e\xe5\xb8\x82')),
                ('experience', models.CharField(default=b'', max_length=50, verbose_name=b'\xe7\xbb\x8f\xe9\xaa\x8c')),
                ('worktype', models.CharField(default=b'', max_length=50, verbose_name=b'\xe5\xb7\xa5\xe4\xbd\x9c\xe6\x80\xa7\xe8\xb4\xa8')),
                ('education', models.CharField(default=b'', max_length=50, verbose_name=b'\xe5\xad\xa6\xe5\x8e\x86')),
                ('address', models.CharField(default=b'', max_length=200, verbose_name=b'\xe5\xb7\xa5\xe4\xbd\x9c\xe5\x9c\xb0\xe7\x82\xb9')),
                ('company', models.CharField(default=b'', max_length=50, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\x8d\xe7\xa7\xb0')),
                ('company_shortname', models.CharField(default=b'', max_length=50, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\x8d\xe7\xa7\xb0')),
                ('company_site', models.CharField(default=b'', max_length=50, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xb8\xbb\xe9\xa1\xb5')),
                ('company_stage', models.CharField(default=b'', max_length=50, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe9\x98\xb6\xe6\xae\xb5')),
                ('industry_area', models.CharField(default=b'', max_length=50, verbose_name=b'\xe8\xa1\x8c\xe4\xb8\x9a\xe9\xa2\x86\xe5\x9f\x9f')),
                ('publish_time', models.DateTimeField(verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x8a\x93\xe5\x8f\x96\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name_plural': '\u804c\u4f4d',
            },
        ),
    ]
