# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0003_auto_20160113_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='kind',
            field=models.IntegerField(default=1, verbose_name=b'\xe9\x80\x9a\xe7\x9f\xa5\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(1, b'\xe6\x96\x87\xe7\xab\xa0,\xe4\xb8\x8d\xe6\x98\xbe\xe7\xa4\xba\xe5\x8e\x9f\xe6\x96\x87\xe9\x93\xbe\xe6\x8e\xa5'), (2, b'URL'), (3, b'\xe6\x96\x87\xe7\xab\xa0,\xe6\x98\xbe\xe7\xa4\xba\xe5\x8e\x9f\xe6\x96\x87\xe9\x93\xbe\xe6\x8e\xa5')]),
        ),
    ]
