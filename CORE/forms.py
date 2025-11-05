from django import forms
from django.contrib.auth.models import User

from .models import *
from Masters.models import *

from smart_selects.db_fields import ChainedForeignKey

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

# --- ADD THIS NEW FORM ---
class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        # We get all fields from the model
        fields = '__all__'

# Employee forms
# ------------------------------------------------------------------
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

class ServiceRecordForm(forms.ModelForm):
    vehicle = ChainedForeignKey(
        Vehicle,
        chained_field="customer",
        chained_model_field="customer",
        show_all=False,
        auto_choose=True,
        sort=True
    )

    class Meta:
        model = Service
        fields = [
            'customer', 
            'vehicle', 
            'mechanic', 
            'status', 
            'description_of_service', 
            'labor_cost'
        ]

class ServiceInvoiceForm(forms.ModelForm):
    service = forms.ModelChoiceField(
        queryset=Service.objects.filter(
            status__in=['COMPLETED', 'BILLED'], 
            invoice__isnull=True
        ).order_by('-service_date')
    )
        
    class Meta:
        model = ServiceInvoice
        fields = [
            'service', 
            'cashier', 
            'payment_method',
            'status'
        ]