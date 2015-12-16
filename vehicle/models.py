# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Bus(models.Model):
    bid = models.CharField(max_length=45)
    plate_number = models.CharField(max_length=45)
    drivers = models.ManyToManyField(User)


class BaseBusData(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()

    class Meta:
        abstract = True


class BusData(BaseBusData):
    STATUS = (
        (0, '静止'),
        (1, "纯电动"),
        (2, "混合动力"),
        (3, "行车充电"),
        (4, "制动回馈"),
    )
    GEAR = (
        (0, 'P'),
        (1, 'R'),
        (2, 'N'),
        (3, 'D'),
    )
    speed = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS, null=True, blank=True)
    gear = models.IntegerField(choices=GEAR, null=True, blank=True)
    failure_info = models.IntegerField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)


class MileageData(BaseBusData):
    total = models.IntegerField(null=True, blank=True)
    section = models.IntegerField(null=True, blank=True)
    remain = models.IntegerField(null=True, blank=True)


    
