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
    speed = models.CharField(_("Speed"), null=True, blank=True, max_length=20)
    status = models.CharField(_("Vehicle status"), null=True, blank=True, max_length=20)
    gear = models.CharField(_("Gear"), null=True, blank=True, max_length=20)
    failure_info = models.CharField(_("Failure information"), null=True, blank=True, max_length=20)
    longitude = models.CharField(_("Longitude"), null=True, blank=True, max_length=20)
    latitude = models.CharField(_("Latitude"), null=True, blank=True, max_length=20)


class MileageData(BaseBusData):
    total = models.CharField(_("Total milage"), null=True, blank=True, max_length=20)
    section = models.CharField(_("Section milage"), null=True, blank=True, max_length=20)
    remain = models.CharField(_("Available milage"), null=True, blank=True, max_length=20)


class GasData(BaseBusData):
    remain = models.CharField(_("Remain hydrogen"), null=True, blank=True, max_length=20)
    bottle_temp = models.CharField(_("Hydrogen bottle temp."), null=True, blank=True, max_length=20)


class FuelCellData(BaseBusData):
    STATUS = (
        # Translators: work / 工作中
        (0, _("work")),
        # Translators: failure / 故障
        (1, _("failure")),
        # Translators: stop / 停止
        (2, _("stop")),
    )
    status = models.CharField(_("Fuel cell status"), null=True, blank=True, max_length=20)
    voltage = models.CharField(_("Fuel cell voltage"), null=True, blank=True, max_length=20)
    current = models.CharField(_("Fuel cell current"), null=True, blank=True, max_length=20)
    temp = models.CharField(_("Fuel cell temperature"), null=True, blank=True, max_length=20)


class PowerBatteryData(BaseBusData):
    status = models.CharField(_("Battery status"), null=True, blank=True, max_length=20)
    voltage = models.CharField(_("Battery voltage"), null=True, blank=True, max_length=20)
    current = models.CharField(_("Battery current"), null=True, blank=True, max_length=20)
    temp = models.CharField(_("Battery temperature"), null=True, blank=True, max_length=20)
    remain = models.CharField(_("Battery left"), null=True, blank=True, max_length=20)


class EnergySavingData(BaseBusData):
    energy_saving_amount = models.CharField(_("Energy saving amount"), null=True, blank=True, max_length=20)
    energy_saving_money = models.CharField(_("Energy saving money"), null=True, blank=True, max_length=20)
    emission_reduction = models.CharField(_("Emission reduction"), null=True, blank=True, max_length=20)


class MotorData(BaseBusData):
    speed = models.CharField(_("Motor speed"), null=True, blank=True, max_length=20)
    torque = models.CharField(_("Motor torque"), null=True, blank=True, max_length=20)
    voltage = models.CharField(_("Motor voltage"), null=True, blank=True, max_length=20)
    current = models.CharField(_("Motor current"), null=True, blank=True, max_length=20)
    temp = models.CharField(_("Motor temperature"), null=True, blank=True, max_length=20)
