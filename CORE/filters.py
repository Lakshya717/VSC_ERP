import django_filters
from .models import Employee, MASTER_role
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