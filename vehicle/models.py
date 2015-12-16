# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Bus(models.Model):
    bid = models.CharField(max_length=45)
    plate_number = models.CharField(max_length=45)


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
    status = models.IntegerField(choices=STATUS)
    speed = models.IntegerField
    gear = models.IntegerField(choices=GEAR)
    failure_info = models.IntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()


    
