# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0002_favorite_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='abstract',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='author',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='originid',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='site',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='tags',
        ),
        migrations.AddField(
            model_name='topic',
            name='kind',
            field=models.IntegerField(default=1, verbose_name=b'\xe9\x80\x9a\xe7\x9f\xa5\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(1, b'\xe6\x96\x87\xe7\xab\xa0'), (2, b'URL')]),
        ),
    ]
