# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import topics.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '\u6536\u85cf',
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe8\x8a\x82\xe7\x82\xb9\xe5\x90\x8d\xe7\xa7\xb0')),
                ('desc', models.TextField(default=b'', verbose_name=b'\xe8\x8a\x82\xe7\x82\xb9\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d')),
            ],
            options={
                'verbose_name_plural': '\u8282\u70b9',
            },
        ),
        migrations.CreateModel(
            name='Reply',
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
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe5\x88\x86\xe5\x8c\xba\xe5\x90\x8d\xe7\xa7\xb0')),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d')),
            ],
            options={
                'verbose_name_plural': '\u5206\u533a',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uniqueid', models.CharField(default=topics.models.get_default_uniqueid, unique=True, max_length=100, verbose_name=b'url\xe7\x9a\x84md5\xe5\x80\xbc')),
                ('url', models.CharField(default=b'', max_length=500, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\x9a\x84url')),
                ('site', models.CharField(default=b'', max_length=200, verbose_name=b'\xe6\x9d\xa5\xe6\xba\x90\xe7\xbd\x91\xe7\xab\x99')),
                ('originid', models.CharField(default=b'', max_length=200, verbose_name=b'\xe6\x9d\xa5\xe6\xba\x90id')),
                ('avatar', models.CharField(default=b'', max_length=500, verbose_name=b'\xe7\xbc\xa9\xe7\x95\xa5\xe5\x9b\xbe\xe5\x9c\xb0\xe5\x9d\x80')),
                ('author', models.CharField(default=b'', max_length=50, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85')),
                ('abstract', models.TextField(default=b'', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\xae\x80\xe4\xbb\x8b')),
                ('title', models.CharField(max_length=200, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('content', models.TextField(default=b'', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x86\x85\xe5\xae\xb9')),
                ('source', models.TextField(default=b'', verbose_name=b'markdown\xe5\x8e\x9f\xe6\xa0\xbc\xe5\xbc\x8f')),
                ('tags', models.CharField(default=b'', max_length=50, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xa0\x87\xe7\xad\xbe,\xe4\xbb\xa5|\xe5\x88\x86\xe5\x89\xb2')),
                ('publish_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('status', models.IntegerField(default=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x98\xbe\xe7\xa4\xba', choices=[(1, b'\xe6\x98\xbe\xe7\xa4\xba'), (2, b'\xe5\x88\xa0\xe9\x99\xa4')])),
                ('replies_count', models.IntegerField(default=0, verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8d\xe6\x9d\xa1\xe6\x95\xb0')),
                ('reply_time', models.DateTimeField(null=True, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe5\x9b\x9e\xe5\xa4\x8d\xe6\x97\xb6\xe9\x97\xb4')),
                ('last_reply_user', models.ForeignKey(related_name='my_replied_topics', verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe5\x9b\x9e\xe5\xa4\x8d\xe4\xba\xba', to=settings.AUTH_USER_MODEL, null=True)),
                ('node', models.ForeignKey(default=8, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe8\x8a\x82\xe7\x82\xb9', to='topics.Node')),
                ('user', models.ForeignKey(related_name='topics', verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.AddField(
            model_name='reply',
            name='topic',
            field=models.ForeignKey(related_name='replies', verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8d\xe7\x9a\x84\xe6\x96\x87\xe7\xab\xa0', to='topics.Topic'),
        ),
        migrations.AddField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(related_name='replies', verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8d\xe4\xba\xba', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='node',
            name='section',
            field=models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe5\x88\x86\xe5\x8c\xba', to='topics.Section'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='topic',
            field=models.ForeignKey(related_name='favorites', verbose_name=b'\xe5\xb8\x96\xe5\xad\x90', to='topics.Topic'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(related_name='favorites', verbose_name=b'\xe6\x94\xb6\xe8\x97\x8f\xe8\x80\x85', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together=set([('user', 'topic')]),
        ),
    ]
