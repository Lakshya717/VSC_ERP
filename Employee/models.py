from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

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
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.ForeignKey(MASTER_role,on_delete=models.SET_NULL,null=True)
    DOB = models.DateField()
    Address = models.TextField()
    mobile_number = PhoneNumberField(region="IN")

    SHIFT_CHOICES = [
        ('MORNING', 'Morning (9AM-5PM)'),
        ('EVENING', 'Evening (1PM-9PM)'),
        ('NIGHT', 'Night (9PM-5AM)'),
        ('FLEX', 'Flexible'),
    ]

    def __str__(self):
        return self.user.get_full_name()

class Mechanic(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    expertise_area = models.ForeignKey(MASTER_expertise_area, on_delete=models.PROTECT)
    years_of_experience = models.PositiveSmallIntegerField(default=0)
    shift = models.CharField(max_length=10, choices=Employee.SHIFT_CHOICES, default='MORNING')
    certifications = models.TextField(blank=True, null=True)
    
    pay_grade = models.ForeignKey(
        MASTER_pay_grade_level, 
        on_delete=models.PROTECT,
        limit_choices_to={'role__name': 'Mechanic'}
    )

    def __str__(self):
        return f"Mechanic: {self.employee.user.get_full_name()}"
    
class Accountant(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    education = models.TextField(blank=True, null=True)
    shift = models.CharField(max_length=10, choices=Employee.SHIFT_CHOICES, default='MORNING')    
    pay_grade = models.ForeignKey(
        MASTER_pay_grade_level, 
        on_delete=models.PROTECT,
        limit_choices_to={'role__name': 'Accountant'}
    )


class Cashier(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    counter_number = models.CharField(max_length=10)
    shift = models.CharField(max_length=10, choices=Employee.SHIFT_CHOICES, default='MORNING')
    
    pay_grade = models.ForeignKey(
        MASTER_pay_grade_level, 
        on_delete=models.PROTECT,
        limit_choices_to={'role__name': 'Cashier'}
    )

    def __str__(self):
        return f"Cashier: {self.employee.user.get_full_name()}"


class Advisor(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    education_desc = models.TextField(blank=True, null=True)

    # CHANGED: This is now a ForeignKey
    pay_grade = models.ForeignKey(
        MASTER_pay_grade_level, 
        on_delete=models.PROTECT,
        limit_choices_to={'role__name': 'Advisor'}
    )

    def __str__(self):
        return f"Advisor: {self.employee.user.get_full_name()}"
    
