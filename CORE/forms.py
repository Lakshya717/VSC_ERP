from django import forms
from django.contrib.auth.models import User

from .models import *

# Customer forms
# ------------------------------------------------------------------
class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user',]


# Employee forms
# ------------------------------------------------------------------
class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['user',]

class MechanicForm(forms.ModelForm):
    class Meta:
        model = Mechanic
        fields = '__all__'
        exclude = ['employee',]

class AccountantForm(forms.ModelForm):
    class Meta:
        model = Accountant
        fields = '__all__'
        exclude = ['employee',]

class CashierForm(forms.ModelForm):
    class Meta:
        model = Cashier
        fields = '__all__'
        exclude = ['employee',]

class AdvisorForm(forms.ModelForm):
    class Meta:
        model = Advisor
        fields = '__all__'
        exclude = ['employee',]


# Inventory forms
# ------------------------------------------------------------------
class SparePartForm(forms.ModelForm):
    class Meta:
        model = SparePart
        fields = '__all__'

class InventoryInvoiceForm(forms.ModelForm):
    class Meta:
        model = InventoryInvoice
        fields = ['spare_part', 'supplier', 'quantity_received', 'cost']


# Service forms
# ------------------------------------------------------------------