from rest_framework import serializers
from renttiApp.models.company import Company
from renttiApp.models.leaseholder import Leaseholder
from renttiApp.serializers.leaseholderSerializer import LeaseholderSerializer

class CompanySerializer (serializers.ModelSerializer):
    leaseholder = LeaseholderSerializer()
    class Meta:
        model = Company
        fields = ['id','nit_rut','username','password','name','office_address','telephone_number','corporate_email','web_site','chamber_of_comerce','leaseholder']

    def create(self, validated_data):
        leaseholderData = validated_data.pop('leaseholder')
        companyInstance = Company.objects.create(**validated_data)
        Leaseholder.objects.create(company_id_id=companyInstance.id, **leaseholderData)
        return companyInstance

    def to_representation(self, obj):
        #through orm from Django gets objects with that id
        company = Company.objects.get(id=obj.id)
        leaseholder = Leaseholder.objects.get(id=obj.id)
        return {    'id':company.id,
                    'nit_rut': company.nit_rut,
                    'username': company.username,
                    'password': company.Password,
                    'name': company.name,
                    'office_address' : company.office_address,
                    'telephone_number': company.telephone_number,
                    'corporate_email': company.corporate_email,
                    'web_site':company.web_site, 
                    'chamber_of_comerce':company.chamber_of_comerce,
                    'leaseholder': {
                        'id': leaseholder.id,
                        'insurance_number': leaseholder.insurance_number
                    } 
                 }