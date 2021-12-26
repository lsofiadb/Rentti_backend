from renttiApp.models.leaseholder import Leaseholder
from rest_framework import serializers

class LeaseholderSerializer (serializers.ModelSerializer):
    class Meta:
        model = Leaseholder
        #ignore foreign key field 
        fields = '__all__' 