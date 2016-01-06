# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0003_auto_20160107_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='node',
            field=models.ForeignKey(default=8, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe8\x8a\x82\xe7\x82\xb9', to='topics.Node'),
        ),
    ]
