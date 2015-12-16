from django.test import TestCase
from .models import Bus, BusData

# Create your tests here.


class BusDataTests(TestCase):

    def test_save(self):
        bus = Bus(bid="hello", plate_number="X32412")
        bus.save()
        self.assertEqual(1, Bus.objects.count())
