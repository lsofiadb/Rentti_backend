from django.db import models
from renttiApp.models.company import Company


class Leaseholder(models.Model):
    #primary key
    id = models.AutoField(primary_key=True)
    #foreign key 
    company_id = models.ForeignKey(Company, related_name='leaseholder', on_delete=models.CASCADE)
    #other attributes
    insurance_number = models.IntegerField('insurance_number')