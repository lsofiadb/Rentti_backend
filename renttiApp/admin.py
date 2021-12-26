from django.contrib import admin

# Register your models here.

from .models.company import Company
from .models.supplier import Supplier
from .models.leaseholder import Leaseholder
from .models.vehicle import Vehicle
from .models.reservation import Reservation


admin.site.register(Company)
admin.site.register(Supplier)
admin.site.register(Leaseholder)
admin.site.register(Vehicle)
admin.site.register(Reservation)
