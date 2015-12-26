# -*- coding: utf-8 -*-

from django.core.cache import cache
from django.forms.models import model_to_dict
from django.shortcuts import _get_queryset
from django.db import models
from models import Bus


def get_object_or_empty(klass, *args, **kwargs):
    """
    When performing `employee = Employee.objects.get(age=90)`,
    If that doesn't exist, you'll get a `Employee.DoesNotExist` exception, which you'll need to catch.
    If there's more than one 99 year-old employee, you'll get a `Employee.MultipleObjectsReturned` exception, which you may want to catch.

    Using this function, you can return an object or {} if object does not exist.
    """
    queryset = _get_queryset(klass)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        return {}


# def latest_or_empty(klass, field_name=None, direction="-"):
#     queryset = _get_queryset(klass)
#     order_by = field_name
#     clone = queryset._clone()
#     clone.query.set_limits(high=1)
#     clone.query.clear_ordering(force_empty=True)
#     clone.query.add_ordering("%s%s" % (direction, order_by))
#     try:
#         return clone.get()
#     except clone.model.DoesNotExist:
#         return {}


def latest_or_empty(klass, field_name=None, direction="-"):
    order_by = field_name
    queryset = _get_queryset(klass)._clone()
    try:
        return queryset.latest(order_by)
    except queryset.model.DoesNotExist:
        return {}


class BusStorage:
    CACHE_KEY_PREFIX = "data:bus:"

    def __init__(self):
        pass

    def get(self, bid):
        """
        get bus data
        :return: dictionary
        """
        data = cache.get(self.CACHE_KEY_PREFIX+bid)
        if data:
            return data
        else:
            data = self.getBusDataFromDB(bid)
            self.set(bid, data)
            return data

    def set(self, bid, data):
        """
        set bus data
        :return:
        """
        cache.set(self.CACHE_KEY_PREFIX+bid, data, None)

    def _to_dict(self, obj, fields=None, exclude=None):
        if type(obj) is dict:
            return obj
        elif isinstance(obj, models.Model):
            return model_to_dict(obj, fields, exclude)
        else:
            return obj.__dict__

    def getBusDataFromDB(self, bid):
        """
        get latest bus data from db
        :param bid:
        :return: dictionary
        """
        # bus = Bus.objects.get(bid=bid)
        # bus_data = bus.busdata_set.latest("timestamp")
        # milage_data = bus.mileagedata_set.latest("timestamp")
        # gas_data = bus.gasdata_set.latest("timestamp")
        # fuel_cell_data = bus.fuelcelldata_set.latest("timestamp")
        # power_battery_data = bus.powerbatterydata_set.latest("timestamp")
        # energy_saving_data = bus.energysavingdata_set.latest("timestamp")
        # motor_data = bus.motordata_set.latest("timestamp")

        try:
            bus = Bus.objects.get(bid=bid)
            bus_data = latest_or_empty(bus.busdata_set, "timestamp");
            milage_data = latest_or_empty(bus.mileagedata_set, "timestamp")
            gas_data = latest_or_empty(bus.gasdata_set, "timestamp")
            fuel_cell_data = latest_or_empty(bus.fuelcelldata_set, "timestamp")
            power_battery_data = latest_or_empty(bus.powerbatterydata_set, "timestamp")
            energy_saving_data = latest_or_empty(bus.energysavingdata_set, "timestamp")
            motor_data = latest_or_empty(bus.motordata_set, "timestamp")

            # turn these objects to dict and return.
            ret = model_to_dict(bus, None, ['drivers', u'id'])
            ret["BusData"] = self._to_dict(bus_data, None, [u'id'])
            ret["MileageData"] = self._to_dict(milage_data, None, [u'id'])
            ret["GasData"] = self._to_dict(gas_data, None, [u'id'])
            ret["FuelCellData"] = self._to_dict(fuel_cell_data, None, [u'id'])
            ret["PowerBatteryData"] = self._to_dict(power_battery_data, None, [u'id'])
            ret["EnergySavingData"] = self._to_dict(energy_saving_data, None, [u'id'])
            ret["MotorData"] = self._to_dict(motor_data, None, [u'id'])
            return ret

        except Bus.DoesNotExist:
            return {}


busStorage = BusStorage()