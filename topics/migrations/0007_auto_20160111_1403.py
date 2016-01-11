# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('topics', '0006_topic_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(default=b'', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x86\x85\xe5\xae\xb9')),
                ('source', models.TextField(default=b'', verbose_name=b'markdown\xe5\x8e\x9f\xe6\xa0\xbc\xe5\xbc\x8f')),
                ('status', models.IntegerField(default=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x98\xbe\xe7\xa4\xba')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('topic', models.ForeignKey(related_name='replies', verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8d\xe7\x9a\x84\xe6\x96\x87\xe7\xab\xa0', to='topics.Topic')),
                ('user', models.ForeignKey(verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8d\xe4\xba\xba', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '\u56de\u590d',
            },
        ),
        migrations.RemoveField(
            model_name='replay',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='replay',
            name='user',
        ),
        migrations.DeleteModel(
            name='Replay',
        ),
    ]
