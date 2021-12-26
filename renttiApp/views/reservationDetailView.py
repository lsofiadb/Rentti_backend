
from rest_framework import generics
from rest_framework.response import Response
from renttiApp.models.reservation import Reservation
from renttiApp.serializers.reservationSerializer import ReservationSerializer

class ReservationDetailView (generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationApi(generics.ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
  
class ReservationDeleteApi(generics.DestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer 
    