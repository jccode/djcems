from rest_framework import viewsets, generics
from models import Beacon
from vehicle.models import Bus
from serializers import BeaconSerializer

# Create your views here.


class BeaconViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Beacon.objects.all()
    serializer_class = BeaconSerializer


class BeaconList(generics.ListAPIView):
    serializer_class = BeaconSerializer

    def get_queryset(self):
        bid = self.kwargs['bid']
        return Bus.objects.get(bid=bid).beacon_set.all()
