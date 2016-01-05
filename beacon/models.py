from __future__ import unicode_literals

from django.utils.translation import ugettext as _
from django.db import models
from vehicle.models import Bus

# Create your models here.


class Beacon(models.Model):
    identifier = models.CharField(_("Identifier"), max_length=45)
    uuid = models.CharField(_("UUID"), max_length=45)
    major = models.IntegerField(_("Major"))
    minor = models.IntegerField(_("Minor"))
    mac = models.CharField(_("MAC"), max_length=45, null=True, blank=True)
    comment = models.CharField(_("Comment"), max_length=45, null=True, blank=True)
    stick_on = models.ManyToManyField(Bus, verbose_name=_("Stick on"), blank=True)
    enabled = models.BooleanField(_("Enabled"), blank=True)


class BeaconCheckIn(models.Model):
    # EVENT = (
    #     (0, _("enter")),
    #     (1, _("leave")),
    #     (2, _("stay")),
    # )
    uid = models.IntegerField(_("User id"))
    bid = models.CharField(_("Bus unique id"), max_length=45)
    #event = models.IntegerField(_("event"), choices=EVENT)
    #timestamp = models.DateTimeField()
    on_time = models.DateTimeField(_("On time"), null=True, blank=True)
    off_time = models.DateTimeField(_("Off time"), null=True, blank=True)
    last_update = models.DateTimeField(_("Last update time"), null=True, blank=True)
    energy_saving_amount = models.IntegerField(_("Energy saving amount"), null=True, blank=True)
    energy_saving_money = models.IntegerField(_("Energy saving money"), null=True, blank=True)
    emission_reduction = models.IntegerField(_("Emission reduction"), null=True, blank=True)
