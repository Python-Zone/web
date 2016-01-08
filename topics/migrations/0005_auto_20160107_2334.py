# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import topics.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('topics', '0004_auto_20160107_0220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Replay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(default=b'', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x86\x85\xe5\xae\xb9')),
                ('source', models.TextField(default=b'', verbose_name=b'markdown\xe5\x8e\x9f\xe6\xa0\xbc\xe5\xbc\x8f')),
                ('status', models.IntegerField(default=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x98\xbe\xe7\xa4\xba')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name_plural': '\u56de\u590d',
            },
        ),
        migrations.AddField(
            model_name='topic',
            name='last_reply_user',
            field=models.ForeignKey(related_name='my_replied_topics', verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe5\x9b\x9e\xe5\xa4\x8d\xe4\xba\xba', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='replies_count',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8d\xe6\x9d\xa1\xe6\x95\xb0'),
        ),
        migrations.AddField(
            model_name='topic',
            name='reply_time',
            field=models.DateTimeField(null=True, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe5\x9b\x9e\xe5\xa4\x8d\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AddField(
            model_name='topic',
            name='source',
            field=models.TextField(default=b'', verbose_name=b'markdown\xe5\x8e\x9f\xe6\xa0\xbc\xe5\xbc\x8f'),
        ),
        migrations.AddField(
            model_name='topic',
            name='user',
            field=models.ForeignKey(related_name='my_topics', verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='author',
            field=models.CharField(default=b'', max_length=50, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='avatar',
            field=models.CharField(default=b'', max_length=500, verbose_name=b'\xe7\xbc\xa9\xe7\x95\xa5\xe5\x9b\xbe\xe5\x9c\xb0\xe5\x9d\x80'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='originid',
            field=models.CharField(default=b'', max_length=200, verbose_name=b'\xe6\x9d\xa5\xe6\xba\x90id'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='publish_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='site',
            field=models.CharField(default=b'', max_length=200, verbose_name=b'\xe6\x9d\xa5\xe6\xba\x90\xe7\xbd\x91\xe7\xab\x99'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='uniqueid',
            field=models.CharField(default=topics.models.get_default_uniqueid, unique=True, max_length=100, verbose_name=b'url\xe7\x9a\x84md5\xe5\x80\xbc'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='url',
            field=models.CharField(default=b'', max_length=500, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\x9a\x84url'),
        ),
        migrations.AddField(
            model_name='replay',
            name='topic',
            field=models.ForeignKey(verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8d\xe7\x9a\x84\xe6\x96\x87\xe7\xab\xa0', to='topics.Topic'),
        ),
        migrations.AddField(
            model_name='replay',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8d\xe4\xba\xba', to=settings.AUTH_USER_MODEL),
        ),
    ]
