# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.IntegerField(null=True, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(10, b'\xe5\x9b\xbd\xe5\x86\x85\xe5\x95\x86\xe4\xb8\x9a\xe7\xbd\x91\xe7\xab\x99'), (20, b'\xe5\x9b\xbd\xe5\x86\x85\xe5\x88\x9b\xe4\xb8\x9a\xe5\x85\xac\xe5\x8f\xb8'), (30, b'\xe5\x9b\xbd\xe5\xa4\x96\xe4\xbc\x81\xe4\xb8\x9a/\xe5\x9b\xa2\xe9\x98\x9f'), (40, b'\xe6\x8a\x80\xe6\x9c\xaf\xe5\x8d\x9a\xe5\xae\xa2'), (50, b'Python\xe7\xa4\xbe\xe5\x8c\xba')])),
                ('name', models.CharField(max_length=100, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('url', models.CharField(max_length=500, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xb8\xbb\xe9\xa1\xb5')),
                ('abstract', models.TextField(default=b'', verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe7\xae\x80\xe4\xbb\x8b')),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x8e\x92\xe5\x90\x8d')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name_plural': '\u9177\u7ad9',
            },
        ),
    ]
