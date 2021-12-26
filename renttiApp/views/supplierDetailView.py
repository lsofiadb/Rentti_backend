from rest_framework import generics
from rest_framework.response import Response
from renttiApp.models.supplier import Supplier
from renttiApp.serializers.supplierSerializer import SupplierSerializer

class SupplierDetailView (generics.CreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplierApi(generics.ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplierUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
  
class SupplierDeleteApi(generics.DestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer 
    