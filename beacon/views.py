from datetime import datetime
from rest_framework import viewsets, generics, permissions, views
from models import Beacon, BeaconCheckIn
from vehicle.models import Bus
from serializers import BeaconSerializer, BeaconCheckinSerializer
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from services import checkinStorage

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
            timestamp = data.get("timestamp")
            bid = data.get("bid")
            uid = request.user.id
            print(serializer.data)

            # enter
            if event is 0:
                data = self.onbus(uid, bid, timestamp)
            elif event is 1:
                self.offbus(uid, bid, timestamp)
            elif event is 2:
                self.staybus(uid, bid, timestamp)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def onbus(self, uid, bid, timestamp):
        print("on bus:")
        data = {
            "uid": uid,
            "bid": bid,
            "on_time": timestamp,
            "energy_saving_amount": 0,
            "energy_saving_money": 0,
            "emission_reduction": 0
        }
        BeaconCheckIn.objects.create(**data)
        checkinStorage.subscribe_busdata(bid, uid)
        return data

    def offbus(self, uid, bid, timestamp):
        print("off bus:")
        checkins = BeaconCheckIn.objects.filter(uid=uid, bid=bid).order_by("-on_time")
        if len(checkins) > 0:
            checkin = checkins[0]
            if checkin.off_time is None:
                checkin.off_time = timestamp
                # get energy saving data from cache
                storage = checkinStorage.unsubscribe_busdata(bid,uid)
                checkin.energy_saving_amount = storage.get("energy_saving_amount", )
                checkin.energy_saving_money = storage.get("energy_saving_money")
                checkin.emission_reduction = storage.get("emission_reduction")
                checkin.save()

    def staybus(self, uid, bid, timestamp):
        print("stay bus:")
        checkins = BeaconCheckIn.objects.filter(uid=uid, bid=bid).order_by("-on_time")
        if len(checkins) > 0:
            checkin = checkins[0]
            on_time = checkin.on_time
            n = timezone.now()
            # already off bus OR over 24 hours
            if checkin.off_time is not None or (n - on_time).total_seconds() > 24 * 3600:
                self.onbus(uid, bid, timestamp)
            else:
                checkin.last_update = timestamp
                checkin.save()
        else:
            self.onbus(uid, bid, timestamp)