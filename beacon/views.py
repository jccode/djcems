from rest_framework import viewsets, generics, permissions
from models import Beacon, BeaconCheckIn
from vehicle.models import Bus
from serializers import BeaconSerializer, BeaconCheckInSerializer

# Create your views here.


class BeaconViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Beacon.objects.filter(enabled=True)
    serializer_class = BeaconSerializer
    permission_classes = (permissions.AllowAny,)


class BeaconCheckInCreate(generics.CreateAPIView):
    queryset = BeaconCheckIn.objects.all()
    serializer_class = BeaconCheckInSerializer


class BeaconList(generics.ListAPIView):
    serializer_class = BeaconSerializer

    def get_queryset(self):
        bid = self.kwargs['bid']
        return Bus.objects.get(bid=bid).beacon_set.all()
