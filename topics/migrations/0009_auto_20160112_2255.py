# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('topics', '0008_auto_20160112_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(related_name='favorites', verbose_name=b'\xe5\xb8\x96\xe5\xad\x90', to='topics.Topic')),
                ('user', models.ForeignKey(related_name='favorites', verbose_name=b'\xe6\x94\xb6\xe8\x97\x8f\xe8\x80\x85', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '\u6536\u85cf',
            },
        ),
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together=set([('user', 'topic')]),
        ),
    ]
