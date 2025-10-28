from django.urls import path
from . import views

app_name = "Customer"
urlpatterns = [
    path('CustomerCreationWizard/', views.CustomerCreationWizard.as_view(), name='CustomerCreationWizard'),
]