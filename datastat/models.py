from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class UserSavingEnergyPerDay(models.Model):
    uid = models.IntegerField(_("User id"))
    timestamp = models.DateField()
    energy_saving_amount = models.IntegerField(_("Energy saving amount"), null=True, blank=True)
    energy_saving_money = models.IntegerField(_("Energy saving money"), null=True, blank=True)
    emission_reduction = models.IntegerField(_("Emission reduction"), null=True, blank=True)
    total_milage = models.FloatField(_("Total milage"), null=True, blank=True)


class UserSavingEnergyPerMonth(models.Model):
    uid = models.IntegerField(_("User id"))
    energy_saving_amount = models.IntegerField(_("Energy saving amount"), null=True, blank=True)
    energy_saving_money = models.IntegerField(_("Energy saving money"), null=True, blank=True)
    emission_reduction = models.IntegerField(_("Emission reduction"), null=True, blank=True)
    total_milage = models.FloatField(_("Total milage"), null=True, blank=True)
    timestamp = models.DateField()
    year = models.IntegerField()
    month = models.IntegerField()
