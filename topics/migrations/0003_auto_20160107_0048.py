# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0002_auto_20160105_0940'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='topic',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AddField(
            model_name='node',
            name='section',
            field=models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe5\x88\x86\xe5\x8c\xba', to='topics.Section'),
        ),
        migrations.AddField(
            model_name='topic',
            name='node',
            field=models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe8\x8a\x82\xe7\x82\xb9', to='topics.Node', null=True),
        ),
    ]
