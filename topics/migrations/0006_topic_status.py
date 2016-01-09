# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0005_auto_20160107_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='status',
            field=models.IntegerField(default=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x98\xbe\xe7\xa4\xba', choices=[(1, b'\xe6\x98\xbe\xe7\xa4\xba'), (2, b'\xe5\x88\xa0\xe9\x99\xa4')]),
        ),
    ]
