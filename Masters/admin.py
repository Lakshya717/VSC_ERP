from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(MASTER_role)
admin.site.register(MASTER_expertise_area)
admin.site.register(MASTER_vehicle_category)
admin.site.register(MASTER_vehicle_brand)
admin.site.register(MASTER_vehicle_model)
admin.site.register(MASTER_spare_part_type)