from django.db import models, transaction
from Masters.models import *

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
