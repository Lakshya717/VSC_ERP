from django.urls import path
from . import views

app_name = "CORE"
urlpatterns = [
    path('CustomerCreationWizard/', views.CustomerCreationWizard.as_view(), name='CustomerCreationWizard'),
    path('EmployeeCreationWizard/', views.EmployeeCreationWizard.as_view(), name='EmployeeCreationWizard'),
    
    path('spare_part_create', views.spare_part_create, name='spare_part_create'),
    path('inventory_invoice_create', views.inventory_invoice_create, name='inventory_invoice_create'),

    path('vehicle_create/', views.vehicle_create, name='vehicle_create'),
    
    path('service_record_create/', views.service_record_create, name='service_record_create'),
    path('service_invoice_create/', views.service_invoice_create, name='service_invoice_create'),

    path("login/",views.login.as_view(),name="login"),
	path("logout/", views.logout, name="logout"),
    
    path("",views.index,name="index"),
    path("inventory/",views.inventory,name="inventory"),
    path("customers/",views.customers,name="customers"),       

    path("employee/",views.employee,name="employee"), 
    path('employee/delete/<int:pk>/', views.employee_delete, name='employee_delete'),      
    path('customer/delete/<int:pk>/', views.customer_delete, name='customer_delete'),
    path('vehicle/delete/<int:pk>/', views.vehicle_delete, name='vehicle_delete'),
    path('spare_part/delete/<int:pk>/', views.spare_part_delete, name='spare_part_delete'),
    path('inventory_invoice/delete/<int:pk>/', views.inventory_invoice_delete, name='inventory_invoice_delete'),
    path('service/delete/<int:pk>/', views.service_delete, name='service_delete'),
    path('service_invoice/cancel/<int:pk>/', views.service_invoice_cancel, name='service_invoice_cancel'),
    
    path("profile/",views.profile,name="profile"),       
    path("services/",views.services,name="services"),       
]