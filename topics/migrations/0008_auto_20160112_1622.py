# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0007_auto_20160111_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(related_name='replies', verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8d\xe4\xba\xba', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='topic',
            name='user',
            field=models.ForeignKey(related_name='topics', verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
