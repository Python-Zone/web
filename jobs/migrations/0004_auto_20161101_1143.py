# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20160204_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='city',
            field=models.CharField(default=b'', max_length=50, verbose_name=b'\xe5\x9f\x8e\xe5\xb8\x82', db_index=True),
        ),
    ]
