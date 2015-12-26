from django.test import TestCase
from .models import Bus, BusData, MileageData
from serializers import BusSerializer, BusDataSerializer
from django.contrib.auth.models import User
from django.utils import timezone

# Create your tests here.


class BusDataTests(TestCase):

    # def __init__(self, *args, **kwargs):
    #     super(TestCase, self).__init__(*args, **kwargs)
    #     self.bus = Bus(bid="hello", plate_number="X32412")

    def setUp(self):
        bus = Bus(bid="hello", plate_number="X32412")
        bus.save()

    def test_save_bus(self):
        self.assertEqual(1, Bus.objects.count())

    def test_save_bus_data(self):
        bus = Bus.objects.get(bid="hello")
        busData = BusData()
        busData.bus = bus
        busData.status = 0
        busData.speed = 100
        busData.gear = 1
        busData.longitude = 22.432
        busData.latitude = 32.111
        busData.timestamp = timezone.now()
        busData.save()
        self.assertEqual(1, BusData.objects.count())

    def test_save_mileage_data(self):
        bus = Bus.objects.get(bid="hello")
        mileage = MileageData(bus=bus)
        mileage.timestamp = timezone.now()
        mileage.total = 1056
        mileage.section = 380
        mileage.remain = 600
        mileage.save()
        self.assertEqual(1, MileageData.objects.count())

    def test_delete(self):
        bus = Bus.objects.get(bid="hello")
        now = timezone.now()
        busData = BusData(bus=bus, timestamp=now)
        mileage = MileageData(bus=bus, timestamp=now)
        busData.save()
        mileage.save()
        self.assertEqual(1, BusData.objects.count())
        self.assertEqual(1, MileageData.objects.count())
        bus.delete()
        self.assertEqual(0, Bus.objects.count())
        self.assertEqual(0, BusData.objects.count())
        self.assertEqual(0, MileageData.objects.count())

    def test_bus_bind_user(self):
        self.assertEqual(1, Bus.objects.count())
        bus = Bus.objects.get(bid="hello")
        user1 = User.objects.create_user('tom', 'tom@fakesite.com', 'tom')
        user2 = User.objects.create_user('cat', 'cat@fakesite.com', 'cat')
        self.assertEqual(2, User.objects.count())
        bus.drivers.add(user1, user2)
        self.assertEqual(2, Bus.objects.get(bid="hello").drivers.count())
