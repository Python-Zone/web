# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wiki',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.IntegerField(null=True, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(10, b'Python \xe5\x85\xa5\xe9\x97\xa8\xe6\x95\x99\xe7\xa8\x8b'), (20, b'Python \xe9\xab\x98\xe7\xba\xa7\xe8\xbf\x9b\xe9\x98\xb6\xe6\x95\x99\xe7\xa8\x8b'), (30, b'Web\xe5\xbc\x80\xe5\x8f\x91'), (40, b'\xe7\xb3\xbb\xe7\xbb\x9f\xe7\xae\xa1\xe7\x90\x86'), (50, b'\xe4\xba\x91\xe8\xae\xa1\xe7\xae\x97/\xe5\xa4\xa7\xe6\x95\xb0\xe6\x8d\xae/\xe6\x9c\xba\xe5\x99\xa8\xe5\xad\xa6\xe4\xb9\xa0'), (60, b'\xe9\x87\x8f\xe5\x8c\x96\xe5\x88\x86\xe6\x9e\x90')])),
                ('title', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('subhead', models.CharField(default=b'', max_length=100, verbose_name=b'\xe5\x89\xaf\xe6\xa0\x87\xe9\xa2\x98', blank=True)),
                ('url', models.CharField(default=b'', max_length=500, verbose_name=b'\xe5\xa4\x96\xe9\x93\xbe', blank=True)),
                ('author', models.CharField(max_length=50, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85')),
                ('content', models.TextField(default=b'', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x86\x85\xe5\xae\xb9', blank=True)),
                ('publish_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x8e\x92\xe5\x90\x8d')),
                ('status', models.IntegerField(default=0, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe5\xb7\xb2\xe5\x8f\x91\xe5\xb8\x83'), (1, b'\xe6\x9c\xaa\xe5\x8f\x91\xe5\xb8\x83'), (2, b'\xe5\xb7\xb2\xe5\x88\xa0\xe9\x99\xa4')])),
            ],
            options={
                'verbose_name_plural': 'wiki',
            },
        ),
    ]
