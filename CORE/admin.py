from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Mechanic)
admin.site.register(Cashier)

admin.site.register(SparePart)
admin.site.register(InventoryInvoice)

admin.site.register(Service)
admin.site.register(ServicePart)
admin.site.register(ServiceInvoice)

