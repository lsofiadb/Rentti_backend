from rest_framework import generics
from rest_framework.response import Response
from renttiApp.models.leaseholder import Leaseholder
from renttiApp.serializers.leaseholderSerializer import LeaseholderSerializer

class LeaseholderDetailView (generics.CreateAPIView):
    queryset = Leaseholder.objects.all()
    serializer_class = LeaseholderSerializer

class LeaseholderApi(generics.ListAPIView):
    queryset = Leaseholder.objects.all()
    serializer_class = LeaseholderSerializer

class LeaseholderUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Leaseholder.objects.all()
    serializer_class = LeaseholderSerializer
  
class LeaseholderDeleteApi(generics.DestroyAPIView):
    queryset = Leaseholder.objects.all()
    serializer_class = LeaseholderSerializer 