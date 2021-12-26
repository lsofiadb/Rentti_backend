from django.db import models
from renttiApp.models.leaseholder import Leaseholder

from renttiApp.models.vehicle import Vehicle

class Reservation(models.Model):
    #primary key 
    id = models.AutoField(primary_key=True)
    #foreign keys
    vehicle_plaque = models.ForeignKey(Vehicle,related_name="reservation_vehicle_plaque", on_delete=models.CASCADE)
    leaseholder_id = models.ForeignKey(Leaseholder, related_name='reservation_leaseholder', on_delete=models.CASCADE)
    #others attributes 
    initial_date = models.DateTimeField()
    final_date = models.DateTimeField()
    total_price = models.FloatField()
    