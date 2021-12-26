from rest_framework import serializers
from renttiApp.models.reservation import Reservation

class ReservationSerializer (serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        
    
    