from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField
from smart_selects.db_fields import ChainedForeignKey

from Masters.models import *

'''
### 1. User

- username
- first_name
- last_name
- email
- password
- is_staff
- is_active
'''

# Employee Models
# ------------------------------------------------------------------

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DOB = models.DateField()
    Address = models.TextField()
    mobile_number = PhoneNumberField(region="IN")

    SHIFT_CHOICES = [
        ('MORNING', 'Morning (9AM-5PM)'),
        ('EVENING', 'Evening (1PM-9PM)'),
        ('NIGHT', 'Night (9PM-5AM)'),
        ('FLEX', 'Flexible'),
    ]
    
    role = models.ForeignKey(MASTER_role, on_delete=models.SET_NULL, null=True)

    shift = models.CharField(
        max_length=10, 
        choices=SHIFT_CHOICES, 
        default='MORNING',
        null=True,
        blank=True 
    )

    pay_grade = ChainedForeignKey(
        MASTER_pay_grade_level,
        chained_field="role",
        chained_model_field="role",
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
class Mechanic(models.Model):
    employee = models.OneToOneField(
        Employee, 
        on_delete=models.CASCADE, 
        primary_key=True,
        limit_choices_to={'role__name': 'Mechanic'}
    )
    
    expertise_area = models.ForeignKey(
        MASTER_expertise_area, 
        on_delete=models.PROTECT,
        limit_choices_to={'role__name': 'Mechanic'}
    )
    
    years_of_experience = models.PositiveSmallIntegerField(default=0)
    certifications = models.TextField(blank=True, null=True)
    
    
class Accountant(models.Model):
    employee = models.OneToOneField(
        Employee, 
        on_delete=models.CASCADE, 
        primary_key=True,
        limit_choices_to={'role__name': 'Accountant'}
    )
    
    education = models.TextField(blank=True, null=True)
    

class Cashier(models.Model):
    employee = models.OneToOneField(
        Employee, 
        on_delete=models.CASCADE, 
        primary_key=True,
        limit_choices_to={'role__name': 'Cashier'}
    )
    
    counter_number = models.CharField(max_length=10)
    

class Advisor(models.Model):
    employee = models.OneToOneField(
        Employee, 
        on_delete=models.CASCADE, 
        primary_key=True,
        limit_choices_to={'role__name': 'Advisor'}
    )
    
    education_desc = models.TextField(blank=True, null=True)
    