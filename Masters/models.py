from django.db import models

# Employee Masters
# ------------------------------------------------------------------
class MASTER_role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class MASTER_pay_grade_level(models.Model):
    role = models.ForeignKey(MASTER_role, on_delete=models.CASCADE)
    level = models.CharField(max_length=10) # e.g., "L1", "L2", "Senior"
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('role', 'level')

    def __str__(self):
        return f"{self.role.name} - {self.level} (${self.base_salary})"

class MASTER_expertise_area(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

# Vehicle Masters
# ------------------------------------------------------------------
class MASTER_vehicle_category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    licence_type = models.CharField(max_length=20, blank=True)
    wheels = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = "MASTER - Vehicle Categories"

    def __str__(self):
        return self.name

class MASTER_vehicle_brand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "MASTER - Vehicle Brands"

    def __str__(self):
        return self.name

class MASTER_vehicle_model(models.Model):
    brand = models.ForeignKey(MASTER_vehicle_brand, on_delete=models.CASCADE, related_name="models")
    category = models.ForeignKey(MASTER_vehicle_category, on_delete=models.PROTECT, related_name="models")
    name = models.CharField(max_length=100)
    engine = models.CharField(max_length=50, blank=True)
    weight = models.PositiveIntegerField(help_text="Weight in kg", blank=True, null=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "MASTER - Vehicle Models"
        unique_together = ('brand', 'name') # A brand can't have two models with the same name

    def __str__(self):
        return f"{self.brand.name} {self.name}"