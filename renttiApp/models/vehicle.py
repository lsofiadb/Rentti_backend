from django.db import models

from renttiApp.models.supplier import Supplier

class Vehicle(models.Model):
    #primary key 
    plate = models.IntegerField(primary_key=True)
    #foreign key 
    supplier_id = models.ForeignKey(Supplier, related_name='vehicle', on_delete=models.CASCADE)
    #other attributes
    model = models.CharField('model',max_length=50)
    brand = models.CharField('brand',max_length=50)
    current_price = models.FloatField('current_price')
    status = models.BooleanField('status',default=False)