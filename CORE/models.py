import datetime

from django.db import models, transaction
from django.contrib.auth.models import User
from django.db.models import Sum, F
from django.core.exceptions import PermissionDenied, ValidationError

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


# Customer Models
# ------------------------------------------------------------------
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
    

# Inventory Models
# ------------------------------------------------------------------
class SparePart(models.Model):
    vehicle_model = models.ForeignKey(
        MASTER_vehicle_model, 
        on_delete=models.CASCADE, 
        related_name="parts"
    )
    
    name = models.CharField(max_length=100)
    
    type = models.ForeignKey(
        MASTER_spare_part_type,
        on_delete=models.PROTECT,
        related_name="parts",
        null=True,
        blank=True
    )

    quantity_in_stock = models.PositiveIntegerField(default=0)
    
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        help_text="Price per unit"
    )

    class Meta:
        verbose_name = "Spare Part"
        verbose_name_plural = "Spare Parts"
        unique_together = ('vehicle_model', 'name') # A model can't have two parts with the same name

    def __str__(self):
        return f"{self.name} for {self.vehicle_model} ({self.quantity_in_stock} in stock)"

class InventoryInvoice(models.Model):
    spare_part = models.ForeignKey(SparePart, on_delete=models.PROTECT, related_name="invoices")
    supplier = models.CharField(max_length=100)
    quantity_received = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    cost = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        help_text="Total cost for this batch"
    )

    class Meta:
        verbose_name = "Inventory Invoice"
        verbose_name_plural = "Inventory Invoices"
        ordering = ['-date']

    def __str__(self):
        return f"Invoice for {self.quantity_received}x {self.spare_part.name} on {self.date.date()}"

    def save(self, *args, **kwargs):
        is_new = self.pk is None 
        
        try:
            with transaction.atomic():
                super().save(*args, **kwargs) 
                if is_new: 
                    part = self.spare_part
                    part.quantity_in_stock += self.quantity_received
                    part.save()
        except Exception as e:
            print(f"Error saving invoice, transaction rolled back: {e}")
            raise

    def delete(self, *args, **kwargs):
        try:
            with transaction.atomic():
                part = self.spare_part
                part.quantity_in_stock -= self.quantity_received
                
                if part.quantity_in_stock < 0:
                    part.quantity_in_stock = 0
                
                part.save()

                super().delete(*args, **kwargs) 
        except Exception as e:
            print(f"Error deleting invoice, transaction rolled back: {e}")
            raise


# Service Models
# ------------------------------------------------------------------
class Service(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('BILLED', 'Billed'),
        ('CANCELLED', 'Cancelled'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="services")
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT, related_name="services")
    
    mechanic = models.ForeignKey(
        Mechanic, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name="services"
    )
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    description_of_service = models.TextField()
    
    labor_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    service_date = models.DateTimeField(auto_now_add=True)

    parts = models.ManyToManyField(
        SparePart,
        through='ServicePart',
        related_name='services_used_in'
    )

    class Meta:
        verbose_name = "Service Record"
        verbose_name_plural = "Service Records"
        ordering = ['-service_date']

    def __str__(self):
        return f"Service {self.id} for {self.vehicle.registration_number}"

    def calculate_total_cost(self):
        parts_total_agg = self.servicepart_set.aggregate(
            total=Sum(F('quantity') * F('unit_price'))
        )
        parts_total = parts_total_agg['total'] or 0.00

        return float(parts_total) + float(self.labor_cost)

class ServicePart(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    part = models.ForeignKey(SparePart, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    
    unit_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        blank=True,
        help_text="Price of the part at the time of service."
    )
    
    _old_quantity = 0

    class Meta:
        verbose_name = "Part Used in Service"
        verbose_name_plural = "Parts Used in Service"
        unique_together = ('service', 'part') 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._old_quantity = self.quantity if self.pk else 0

    def __str__(self):
        return f"{self.quantity}x {self.part.name} for Service {self.service.id}"
        
    def save(self, *args, **kwargs):
        try:
            with transaction.atomic():
                part = self.part
                
                if self.pk is None and self.unit_price is None:
                    self.unit_price = part.price
                
                diff = self.quantity - self._old_quantity

                if diff > 0 and part.quantity_in_stock < diff:
                    raise ValidationError(
                        f"Not enough stock for {part.name}. "
                        f"Only {part.quantity_in_stock} available."
                    )
                
                part.quantity_in_stock -= diff
                part.save()
                
                super().save(*args, **kwargs)
                
                self._old_quantity = self.quantity
                
        except Exception as e:
            print(f"Error in ServicePart save: {e}")
            raise

    def delete(self, *args, **kwargs):
        try:
            with transaction.atomic():
                part = self.part
                
                part.quantity_in_stock += self.quantity
                part.save()
                
                super().delete(*args, **kwargs)
                
        except Exception as e:
            print(f"Error in ServicePart delete: {e}")
            raise # Re-raise the exception to stop the delete

class ServiceInvoice(models.Model):    
    
    service = models.OneToOneField(
        Service, 
        on_delete=models.PROTECT, 
        related_name="invoice"
    )
    cashier = models.ForeignKey(
        Cashier, 
        on_delete=models.PROTECT, 
        related_name="invoices_generated"
    )
    date = models.DateTimeField(auto_now_add=True)
    
    # This amount is locked in on creation
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        help_text="Final amount for this service, calculated on creation."
    )
    
    payment_method = models.CharField(
        max_length=10, 
        choices=[
            ('CASH', 'Cash'),
            ('CARD', 'Card'),
            ('ONLINE', 'Online'),
            ('PENDING', 'Pending'),
        ], 
        default='PENDING'
    )

    status = models.CharField(
        max_length=10, 
        choices=[
            ('PENDING', 'Pending'),
            ('PAID', 'Paid'),
            ('CANCELLED', 'Cancelled'),
        ], 
        default='PENDING'
    )

    # --- Model Settings ---
    class Meta:
        verbose_name = "Service Invoice"
        verbose_name_plural = "Service Invoices"
        ordering = ['-date']

    def __str__(self):
        return f"Invoice {self.id} for Service {self.service.id} (${self.amount})"

    # --- Custom "Smart" Logic ---

    def save(self, *args, **kwargs):
        is_new = self.pk is None # Our "one-time" gate

        try:
            # "all-or-nothing" safety box
            with transaction.atomic():
                
                # This logic runs ONLY when the invoice is first created
                if is_new:
                    service = self.service
                    
                    # --- 1. Calculate and set the amount ---
                    # Calls the method on the Service model
                    total_cost = service.calculate_total_cost()
                    self.amount = total_cost

                    # --- 2. Update the Service status ---
                    # This "closes the loop" on the service.
                    service.status = 'BILLED'
                    service.save()

                # --- 3. Save the invoice itself ---
                super().save(*args, **kwargs)

        except Exception as e:
            print(f"Error saving invoice, transaction rolled back: {e}")
            raise

    def delete(self, *args, **kwargs):
        # ---
        # Deleting a financial record is bad practice.
        # We will block it.
        # ---
        raise PermissionDenied("Service Invoices cannot be deleted. Please set status to 'Cancelled' instead.")
