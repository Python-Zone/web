# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_favorite_follow_notification'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together=set([('user', 'topic')]),
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set([('from_user', 'to_user')]),
        ),
    ]
