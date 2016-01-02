from django.contrib import admin
from models import Beacon

# Register your models here.

@admin.register(Beacon)
class BeaconAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'uuid', 'major', 'minor', 'comment', 'enabled')
