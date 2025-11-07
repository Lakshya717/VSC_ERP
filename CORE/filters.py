import django_filters
from .models import (
    Employee,
    Customer,
    Vehicle,
    SparePart,
    InventoryInvoice,
    Service,
    ServiceInvoice,
    MASTER_role,
)
from django.contrib.auth import get_user_model

User = get_user_model()

class EmployeeFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(
        field_name='user__first_name', 
        lookup_expr='icontains',
        label='First Name'
    )

    last_name = django_filters.CharFilter(
        field_name='user__last_name', 
        lookup_expr='icontains',
        label='Last Name'
    )

    class Meta:
        model = Employee
        fields = ['role', 'shift', 'first_name', 'last_name']


class CustomerFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(
        field_name='user__first_name',
        lookup_expr='icontains',
        label='First Name'
    )
    last_name = django_filters.CharFilter(
        field_name='user__last_name',
        lookup_expr='icontains',
        label='Last Name'
    )
    email = django_filters.CharFilter(
        field_name='user__email',
        lookup_expr='icontains',
        label='Email'
    )

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email']


class SparePartFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        label='Part Name'
    )
    vehicle_model = django_filters.ModelChoiceFilter(
        queryset=SparePart.objects.none(),
        label='Vehicle Model'
    )
    type = django_filters.ModelChoiceFilter(
        queryset=SparePart.objects.none(),
        label='Part Type'
    )

    class Meta:
        model = SparePart
        fields = ['name', 'vehicle_model', 'type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Populate dynamic querysets to avoid import cycles
        self.filters['vehicle_model'].queryset = SparePart._meta.get_field('vehicle_model').related_model.objects.all()
        self.filters['type'].queryset = SparePart._meta.get_field('type').related_model.objects.all()


class InventoryInvoiceFilter(django_filters.FilterSet):
    spare_part = django_filters.ModelChoiceFilter(
        queryset=SparePart.objects.all(),
        label='Spare Part'
    )
    supplier = django_filters.CharFilter(
        field_name='supplier',
        lookup_expr='icontains',
        label='Supplier'
    )
    date = django_filters.DateFromToRangeFilter(
        field_name='date',
        label='Date Range'
    )

    class Meta:
        model = InventoryInvoice
        fields = ['spare_part', 'supplier', 'date']


class ServiceFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(
        field_name='status', choices=Service._meta.get_field('status').choices
    )
    customer_name = django_filters.CharFilter(
        field_name='customer__user__first_name',
        lookup_expr='icontains',
        label='Customer First Name'
    )
    vehicle_reg = django_filters.CharFilter(
        field_name='vehicle__registration_number',
        lookup_expr='icontains',
        label='Vehicle Registration'
    )
    mechanic_name = django_filters.CharFilter(
        field_name='mechanic__employee__user__first_name',
        lookup_expr='icontains',
        label='Mechanic First Name'
    )
    service_date = django_filters.DateFromToRangeFilter(
        field_name='service_date', label='Service Date Range'
    )

    class Meta:
        model = Service
        fields = ['status', 'customer_name', 'vehicle_reg', 'mechanic_name', 'service_date']


class ServiceInvoiceFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(
        field_name='status', choices=ServiceInvoice._meta.get_field('status').choices
    )
    payment_method = django_filters.ChoiceFilter(
        field_name='payment_method', choices=ServiceInvoice._meta.get_field('payment_method').choices
    )
    date = django_filters.DateFromToRangeFilter(field_name='date', label='Date Range')
    customer_name = django_filters.CharFilter(
        field_name='service__customer__user__first_name',
        lookup_expr='icontains',
        label='Customer First Name'
    )

    class Meta:
        model = ServiceInvoice
        fields = ['status', 'payment_method', 'date', 'customer_name']


class VehicleFilter(django_filters.FilterSet):
    registration_number = django_filters.CharFilter(
        field_name='registration_number', lookup_expr='icontains', label='Registration'
    )
    brand = django_filters.ModelChoiceFilter(
        field_name='model__brand',
        queryset=Vehicle._meta.get_field('model').related_model._meta.get_field('brand').related_model.objects.all(),
        label='Brand'
    )
    model = django_filters.ModelChoiceFilter(
        field_name='model',
        queryset=Vehicle._meta.get_field('model').related_model.objects.all(),
        label='Model'
    )
    year = django_filters.RangeFilter(field_name='year', label='Year Range')
    customer_name = django_filters.CharFilter(
        field_name='customer__user__first_name', lookup_expr='icontains', label='Customer First Name'
    )

    class Meta:
        model = Vehicle
        fields = ['registration_number', 'brand', 'model', 'year', 'customer_name']