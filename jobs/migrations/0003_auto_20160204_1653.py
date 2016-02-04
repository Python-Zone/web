# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20160204_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='industry_area',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'\xe8\xa1\x8c\xe4\xb8\x9a\xe9\xa2\x86\xe5\x9f\x9f'),
        ),
    ]
