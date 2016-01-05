from rest_framework import viewsets, generics, permissions, views
from models import Beacon, BeaconCheckIn
from vehicle.models import Bus
from serializers import BeaconSerializer, BeaconCheckinSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class BeaconViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Beacon.objects.filter(enabled=True)
    serializer_class = BeaconSerializer
    permission_classes = (permissions.AllowAny,)


# class BeaconCheckInCreate(generics.CreateAPIView):
#     queryset = BeaconCheckIn.objects.all()
#     serializer_class = BeaconCheckInSerializer



class BeaconList(generics.ListAPIView):
    serializer_class = BeaconSerializer

    def get_queryset(self):
        bid = self.kwargs['bid']
        return Bus.objects.get(bid=bid).beacon_set.all()


class BeaconCheckin(views.APIView):

    def post(self, request, format=None):
        serializer = BeaconCheckinSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            event = data.get("event")
            print(serializer.data)
            # enter
            if event is 0:
                data = self.onbus(data)
            elif event is 1:
                self.offbus(data)
            elif event is 2:
                self.staybus(data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def onbus(self, data):
        print("on bus:")
        data["on_time"] = data.get("timestamp")
        data["energy_saving_amount"] = 0
        data["energy_saving_money"] = 0
        data["emission_reduction"] = 0
        BeaconCheckIn.objects.create(**data)
        return data

    def offbus(self, data):
        print("off bus:")
        checkins = BeaconCheckIn.objects.filter(uid=data.get("uid"), bid=data.get("bid")).order_by("-on_time")
        if len(checkins) > 0:
            checkin = checkins[0]
            if checkin.off_time is None:
                data["off_time"] = data.get("timestamp")
                #

    def staybus(self, data):
        print("stay bus:"+data)
