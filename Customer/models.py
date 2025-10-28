import datetime

from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

from Masters.models import *

class Customer(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        primary_key=True  # Makes the user the primary key for this table
    )
    mobile_number = PhoneNumberField(
        region="IN", 
        blank=False, 
        null=False,
        help_text="Customer's primary contact number"
    )
    address = models.TextField(
        blank=True, 
        null=True,
        help_text="Customer's full mailing address"
    )
    description = models.TextField(
        blank=True, 
        null=True, 
        help_text="Internal notes about the customer (e.g., 'V.I.P.', 'Prefers afternoon calls')"
    )

    def __str__(self):   
        return self.user.get_full_name()

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
