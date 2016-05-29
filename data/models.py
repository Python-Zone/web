# -*- coding: utf-8 -*-
from django.db import models

class Community(models.Model):
    uniqueid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    community_name = models.CharField(max_length=255, blank=True, null=True)
    community_complete_year = models.IntegerField(blank=True, null=True)
    building_density = models.FloatField(blank=True, null=True)
    building_type = models.CharField(max_length=255, blank=True, null=True)
    house_count = models.IntegerField(blank=True, null=True)
    building_count = models.IntegerField(blank=True, null=True)
    green_rate = models.FloatField(blank=True, null=True)
    avr_price = models.FloatField(blank=True, null=True)
    manage_company = models.CharField(max_length=255, blank=True, null=True)
    develop_company = models.CharField(max_length=255, blank=True, null=True)
    price_trend = models.TextField(blank=True, null=True)  # This field type is a guess.
    sell_trend = models.TextField(blank=True, null=True)  # This field type is a guess.
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    school_district_name = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beijing_house_lianjia_communities'
        verbose_name_plural = "小区"