# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uniqueid', models.CharField(max_length=255, unique=True, null=True, blank=True)),
                ('url', models.CharField(max_length=255, null=True, blank=True)),
                ('community_name', models.CharField(max_length=255, null=True, blank=True)),
                ('community_complete_year', models.IntegerField(null=True, blank=True)),
                ('building_density', models.FloatField(null=True, blank=True)),
                ('building_type', models.CharField(max_length=255, null=True, blank=True)),
                ('house_count', models.IntegerField(null=True, blank=True)),
                ('building_count', models.IntegerField(null=True, blank=True)),
                ('green_rate', models.FloatField(null=True, blank=True)),
                ('avr_price', models.FloatField(null=True, blank=True)),
                ('manage_company', models.CharField(max_length=255, null=True, blank=True)),
                ('develop_company', models.CharField(max_length=255, null=True, blank=True)),
                ('price_trend', models.TextField(null=True, blank=True)),
                ('sell_trend', models.TextField(null=True, blank=True)),
                ('lat', models.FloatField(null=True, blank=True)),
                ('lng', models.FloatField(null=True, blank=True)),
                ('school_district_name', models.CharField(max_length=255, null=True, blank=True)),
                ('create_time', models.DateTimeField(null=True, blank=True)),
                ('update_time', models.DateTimeField(null=True, blank=True)),
                ('address', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'db_table': 'beijing_house_lianjia_communities',
                'managed': False,
                'verbose_name_plural': '\u5c0f\u533a',
            },
        ),
    ]
