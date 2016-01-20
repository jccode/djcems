from django.contrib import admin
from django.contrib.auth.models import User
from models import Bus, BusData, MileageData, GasData, FuelCellData, PowerBatteryData, EnergySavingData, MotorData


class BusAdmin(admin.ModelAdmin):
    list_display = ('bid', 'plate_number')

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == "drivers":
            kwargs["queryset"] = User.objects.filter(is_staff=True).filter(groups__name="driver")
        return super(BusAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)


# Register your models here.
admin.site.register(Bus, BusAdmin)


class ReadOnlyAdmin(admin.ModelAdmin):
    actions = None
    list_display_links = None

    def has_add_permission(self, request):
        # Nobody is allowed to add
        return False

    def has_delete_permission(self, request, obj=None):
        # Nobody is allowed to delete
        return False


@admin.register(BusData)
class BusDataAdmin(ReadOnlyAdmin):
    list_display = ('bus', 'timestamp', 'speed', 'status', 'gear', 'failure_info', 'longitude', 'latitude',)


@admin.register(MileageData)
class MileageDataAdmin(ReadOnlyAdmin):
    list_display = ('bus', 'timestamp', 'total', 'section', 'remain',)


@admin.register(GasData)
class GasDataAdmin(ReadOnlyAdmin):
    list_display = ('bus', 'timestamp', 'remain', 'bottle_temp', )


@admin.register(FuelCellData)
class FuelCellDataAdmin(ReadOnlyAdmin):
    list_display = ('bus', 'timestamp', 'status', 'voltage', 'current', 'temp',)


@admin.register(PowerBatteryData)
class PowerBatteryDataAdmin(ReadOnlyAdmin):
    list_display = ('bus', 'timestamp', 'status', 'voltage', 'current', 'temp', 'remain', )


@admin.register(EnergySavingData)
class EnergySavingDataAdmin(ReadOnlyAdmin):
    list_display = ('bus', 'timestamp', 'energy_saving_amount', 'energy_saving_money', 'emission_reduction', )


