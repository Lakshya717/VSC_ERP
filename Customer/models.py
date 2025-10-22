from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

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
