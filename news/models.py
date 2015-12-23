from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
from userprofile.models import UserProfile
from tinymce import models as tinymce_models

# Create your models here.


class News(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    author = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, verbose_name=_("Author"))
    timestamp = models.DateTimeField(_("Create time"), auto_now_add=True)
    brief = models.TextField(_("Brief"))
    content = tinymce_models.HTMLField(_("Content"))
    headimg = models.ImageField(_("Head image"))
    published = models.BooleanField(_("Published"))

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')