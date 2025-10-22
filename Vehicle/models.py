from django.db import models
import datetime

from Masters.models import *
from Customer.models import Customer

def get_current_year():
    return datetime.date.today().year

class Vehicle(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="vehicles")
    registration_number = models.CharField(max_length=20, unique=True)
    chassis_number = models.CharField(max_length=17, unique=True)
    model = models.ForeignKey(MASTER_vehicle_model, on_delete=models.PROTECT, related_name="vehicles")
    year = models.PositiveSmallIntegerField(
        help_text="Year of manufacture",
        default=get_current_year
    )
    description = models.TextField(blank=True, help_text="e.g., Color, dents, or other notes")

    def __str__(self):
        return f"{self.registration_number} ({self.model.brand.name} {self.model.name})"
