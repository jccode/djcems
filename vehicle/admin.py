from django.contrib import admin
from django import forms
from django.contrib.auth.models import User
from models import Bus


class BusAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == "drivers":
            kwargs["queryset"] = User.objects.filter(is_staff=True)
        return super(BusAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

# Register your models here.
admin.site.register(Bus, BusAdmin)

