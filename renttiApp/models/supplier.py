from django.db import models
#from renttiApp.models.company import Company
from .company import Company

class Supplier(models.Model):
    #primary key 
    id = models.AutoField(primary_key=True)
    #foreign key 
    company_id = models.ForeignKey(Company, related_name='supplier', on_delete=models.CASCADE)
    #other attributes 
    commercial_agent_name = models.CharField('commercial_agent_name',max_length=50)
    agent_telephone_number = models.IntegerField('agent_telephone_number')
    agent_email_address = models.CharField('agent_email_address',max_length=50)
    score = models.FloatField('score')
