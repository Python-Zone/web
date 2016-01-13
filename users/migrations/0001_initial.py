# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('nickname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True, null=True)),
                ('avatar', models.CharField(default=b'', max_length=200, null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(related_name='following', verbose_name=b'\xe6\xad\xa3\xe5\x9c\xa8\xe5\x85\xb3\xe6\xb3\xa8', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(related_name='followers', verbose_name=b'\xe5\x85\xb3\xe6\xb3\xa8\xe8\x80\x85', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '\u5173\u6ce8',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.IntegerField(verbose_name=b'\xe9\x80\x9a\xe7\x9f\xa5\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(1, b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x96\x87\xe7\xab\xa0'), (2, b'\xe5\x9b\x9e\xe5\xa4\x8d\xe6\x96\x87\xe7\xab\xa0'), (3, b'\xe5\x85\xb3\xe6\xb3\xa8\xe6\x88\x91')])),
                ('status', models.IntegerField(default=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(1, b'\xe6\x9c\xaa\xe8\xaf\xbb'), (2, b'\xe5\xb7\xb2\xe8\xaf\xbb'), (3, b'\xe5\x88\xa0\xe9\x99\xa4')])),
                ('content', models.TextField(default=b'', verbose_name=b'\xe9\x80\x9a\xe7\x9f\xa5\xe5\x86\x85\xe5\xae\xb9')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('user', models.ForeignKey(related_name='notifications', verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '\u901a\u77e5',
            },
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set([('from_user', 'to_user')]),
        ),
    ]
