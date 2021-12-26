from rest_framework import generics
from rest_framework.response import Response
from renttiApp.models.vehicle import Vehicle
from renttiApp.serializers.vehicleSerializer import VehicleSerializer

class VehicleDetailView (generics.CreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class VehicleApi(generics.ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
  
class VehicleDeleteApi(generics.DestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer 
    
    