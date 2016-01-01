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
