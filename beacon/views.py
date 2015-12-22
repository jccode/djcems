from rest_framework import viewsets
from models import Beacon
from serializers import BeaconSerializer

# Create your views here.


class BeaconViewSet(viewsets.ModelViewSet):
    queryset = Beacon.objects.all()
    serializer_class = BeaconSerializer
