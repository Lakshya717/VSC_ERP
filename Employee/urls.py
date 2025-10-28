from django.urls import path
from . import views

app_name = "Employee"
urlpatterns = [
    path('EmployeeCreationWizard/', views.EmployeeCreationWizard.as_view(), name='EmployeeCreationWizard'),
]