# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='company_shortname',
        ),
        migrations.RemoveField(
            model_name='job',
            name='education',
        ),
        migrations.RemoveField(
            model_name='job',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='job',
            name='originid',
        ),
        migrations.RemoveField(
            model_name='job',
            name='site',
        ),
        migrations.RemoveField(
            model_name='job',
            name='worktype',
        ),
    ]
