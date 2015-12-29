# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='avatar',
            field=models.CharField(default='', max_length=500, verbose_name=b'\xe7\xbc\xa9\xe7\x95\xa5\xe5\x9b\xbe\xe5\x9c\xb0\xe5\x9d\x80'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='originid',
            field=models.CharField(default='', max_length=200, verbose_name=b'\xe6\x9d\xa5\xe6\xba\x90id'),
            preserve_default=False,
        ),
    ]
