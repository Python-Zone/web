# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(verbose_name=b'\xe5\x8f\x82\xe6\x95\xb0\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('value', models.TextField(null=True, verbose_name=b'\xe5\x8f\x82\xe6\x95\xb0\xe5\x80\xbc')),
            ],
        ),
    ]
