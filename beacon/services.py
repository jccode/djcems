# -*- coding: utf-8 -*-

from django.core.cache import cache
import logging


logger = logging.getLogger(__name__)


class BeaconCheckinStorage:
    CACHE_KEY_PREFIX = "data:bus_checkin:"

    def __init__(self):
        pass

    def subscribe_busdata(self, bid, uid):
        storage = self._get_cache(bid)
        if uid not in storage:
            storage[uid] = {
                "energy_saving_amount": 0,
                "energy_saving_money": 0,
                "emission_reduction": 0,
            }
            self._set_cache(bid, storage)
        return storage

    def unsubscribe_busdata(self, bid, uid):
        storage = self._get_cache(bid)
        try:
            data = storage.pop(uid)
            self._set_cache(bid, storage)
            return data
        except KeyError:
            return {}

    def publish_busdata(self, bid, busdata):
        storage = self._get_cache(bid)
        for uid, udata in storage.items():
            try:
                udata["energy_saving_amount"] += float(busdata["energy_saving_amount"])
                udata["energy_saving_money"] += float(busdata["energy_saving_money"])
                udata["emission_reduction"] += float(busdata["emission_reduction"])
            except ValueError:
                pass
            storage[uid] = udata
        self._set_cache(bid, storage)
        return storage

    def get(self, bid, uid):
        return self._get_cache(bid).get(uid)

    def _get_cache(self, bid):
        data = cache.get(self.CACHE_KEY_PREFIX + bid)
        if not data:
            data = {}
            self._set_cache(bid, data)
        return data

    def _set_cache(self, bid, data):
        cache.set(self.CACHE_KEY_PREFIX + bid, data, None)


checkinStorage = BeaconCheckinStorage()