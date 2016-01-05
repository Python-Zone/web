# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wiki',
            name='content',
            field=models.TextField(default=b'', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x86\x85\xe5\xae\xb9', blank=True),
        ),
        migrations.AlterField(
            model_name='wiki',
            name='subhead',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'\xe5\x89\xaf\xe6\xa0\x87\xe9\xa2\x98', blank=True),
        ),
        migrations.AlterField(
            model_name='wiki',
            name='url',
            field=models.CharField(default=b'', max_length=500, verbose_name=b'\xe5\xa4\x96\xe9\x93\xbe', blank=True),
        ),
    ]
