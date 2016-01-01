# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

# Create your models here.


class Bus(models.Model):
    bid = models.CharField(_("Bus unique id"), max_length=45)
    plate_number = models.CharField(_("Plate number"), max_length=45)
    drivers = models.ManyToManyField(User, verbose_name=_("Drivers"), blank=True)

    @property
    def busdata(self):
        return self.busdata_set.latest('timestamp')

    def __unicode__(self):
        return "Bus (%s, %s)" % (self.bid, self.plate_number)

    class Meta:
        verbose_name = _("Bus")
        verbose_name_plural = _("Buses")


class BaseBusData(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()

    class Meta:
        abstract = True


class BusData(BaseBusData):
    STATUS = (
        # Translators: motionless / "静止"
        (0, _("motionless")),
        # Translators: EV / "纯电动"
        (1, _("EV")),
        # Translators: HEV / "混合动力"
        (2, _("HEV")),
        # Translators: Road charging / "行车充电"
        (3, _("Road charging")),
        # Translators: Back braking / 制动回馈
        (4, _("Back braking")),
    )
    GEAR = (
        (0, 'P'),
        (1, 'R'),
        (2, 'N'),
        (3, 'D'),
    )
    speed = models.IntegerField(_("Speed"), null=True, blank=True)
    status = models.IntegerField(_("Vehicle status"), choices=STATUS, null=True, blank=True)
    gear = models.IntegerField(_("Gear"), choices=GEAR, null=True, blank=True)
    failure_info = models.IntegerField(_("Failure information"), null=True, blank=True)
    longitude = models.FloatField(_("Longitude"), null=True, blank=True)
    latitude = models.FloatField(_("Latitude"), null=True, blank=True)


class MileageData(BaseBusData):
    total = models.IntegerField(_("Total milage"), null=True, blank=True)
    section = models.IntegerField(_("Section milage"), null=True, blank=True)
    remain = models.IntegerField(_("Available milage"), null=True, blank=True)


class GasData(BaseBusData):
    remain = models.IntegerField(_("Remain hydrogen"), null=True, blank=True)
    bottle_temp = models.IntegerField(_("Hydrogen bottle temp."), null=True, blank=True)


class FuelCellData(BaseBusData):
    STATUS = (
        # Translators: work / 工作中
        (0, _("work")),
        # Translators: failure / 故障
        (1, _("failure")),
        # Translators: stop / 停止
        (2, _("stop")),
    )
    status = models.IntegerField(_("Fuel cell status"), choices=STATUS, null=True, blank=True)
    voltage = models.IntegerField(_("Fuel cell voltage"), null=True, blank=True)
    current = models.IntegerField(_("Fuel cell current"), null=True, blank=True)
    temp = models.IntegerField(_("Fuel cell temperature"), null=True, blank=True)


class PowerBatteryData(BaseBusData):
    status = models.IntegerField(_("Battery status"), null=True, blank=True)
    voltage = models.IntegerField(_("Battery voltage"), null=True, blank=True)
    current = models.IntegerField(_("Battery current"), null=True, blank=True)
    temp = models.IntegerField(_("Battery temperature"), null=True, blank=True)
    remain = models.IntegerField(_("Battery left"), null=True, blank=True)


class EnergySavingData(BaseBusData):
    energy_saving_amount = models.IntegerField(_("Energy saving amount"), null=True, blank=True)
    energy_saving_money = models.IntegerField(_("Energy saving money"), null=True, blank=True)
    emission_reduction = models.IntegerField(_("Emission reduction"), null=True, blank=True)


class MotorData(BaseBusData):
    speed = models.IntegerField(_("Motor speed"), null=True, blank=True)
    torque = models.IntegerField(_("Motor torque"), null=True, blank=True)
    voltage = models.IntegerField(_("Motor voltage"), null=True, blank=True)
    current = models.IntegerField(_("Motor current"), null=True, blank=True)
    temp = models.IntegerField(_("Motor temperature"), null=True, blank=True)
