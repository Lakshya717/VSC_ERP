from formtools.wizard.views import SessionWizardView
from django.shortcuts import render
from django.forms import Form

from .forms import *

# --- IMPORT SECTION ---
from .models import (
    Customer, 
    Employee, 
    Mechanic, 
    Accountant, 
    Cashier, 
    Advisor, 
    SparePart, 
    InventoryInvoice, 
    Vehicle, 
    Service,
    ServicePart,
    ServiceInvoice
)
from Masters.models import (
    MASTER_role,
    MASTER_pay_grade_level,
    MASTER_expertise_area,
    MASTER_vehicle_category,
    MASTER_vehicle_brand,
    MASTER_vehicle_model,
    MASTER_spare_part_type
)
# --- END OF IMPORT SECTION ---

from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.utils.decorators import method_decorator


@method_decorator(xframe_options_sameorigin, name='dispatch')
class CustomerCreationWizard(SessionWizardView):
    form_list = [
        ("user", UserCreateForm),
        ("customer", CustomerForm),
    ]
    
    TEMPLATES = {
        "user": "customer/wizards/customer_step_user.html",
        "customer": "customer/wizards/customer_step_details.html",
    }

    def get_template_names(self):
        return [self.TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        user_form = form_list[0]
        customer_form = form_list[1]
        user = user_form.save(commit=False)
        user.set_password(user_form.cleaned_data['password'])         
        user.save()
        customer = customer_form.save(commit=False)
        customer.user = user
        customer.save() 
        return render(self.request, 'customer/wizards/customer_wizard_done.html', {
            'username': user.get_full_name()
        })


@method_decorator(xframe_options_sameorigin, name='dispatch')
class EmployeeCreationWizard(SessionWizardView):
    form_list = [
        ("user", UserCreateForm),
        ("employee", EmployeeForm),
        ("role_details", Form),
    ]
    TEMPLATES = {
        "user": "employee/wizards/employee_step_user.html",
        "employee": "employee/wizards/employee_step_employee.html",
        "role_details": "employee/wizards/employee_step_role.html",
    }    
    def get_template_names(self):
        return [self.TEMPLATES[self.steps.current]]
    def get_form(self, step=None, data=None, files=None):        
        if step is None:
            step = self.steps.current
        if step == 'role_details':
            employee_data = self.get_cleaned_data_for_step('employee')
            if employee_data:
                role = employee_data.get('role') 
                if role.name == 'Mechanic':
                    self.form_list[step] = MechanicForm
                elif role.name == 'Accountant':
                    self.form_list[step] = AccountantForm
                elif role.name == 'Cashier':
                    self.form_list[step] = CashierForm
                elif role.name == 'Advisor':
                    self.form_list[step] = AdvisorForm
                else:
                    self.form_list[step] = Form
        return super().get_form(step, data, files)
    def done(self, form_list, **kwargs):
        user_form = form_list[0]
        employee_form = form_list[1]
        role_form = form_list[2]
        user = user_form.save(commit=False)
        user.set_password(user_form.cleaned_data['password'])
        user.save()
        employee = employee_form.save(commit=False)
        employee.user = user
        employee.save() 
        if not isinstance(role_form, Form):
            role_model = role_form.save(commit=False)
            role_model.employee = employee 
            role_model.save()
        return render(self.request, 'employee/wizards/employee_wizard_done.html', {
            'username': user.username
        })

@xframe_options_sameorigin
def spare_part_create(request):
    if request.method == 'POST':
        form = SparePartForm(request.POST)
        if form.is_valid():
            part = form.save()
            return render(request, 'inventory/inventory_part_done.html', {
                'part_name': part.name
            })
    else:
        form = SparePartForm()
    
    return render(request, 'inventory/inventory_form_base.html', {
        'form': form,
        'title': 'Add New Part to Catalog'
    })


@xframe_options_sameorigin
def inventory_invoice_create(request):
    if request.method == 'POST':
        form = InventoryInvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save()
            return render(request, 'inventory/inventory_invoice_done.html', {
                'invoice': invoice
            })
    else:
        form = InventoryInvoiceForm()
    
    return render(request, 'inventory/inventory_form_base.html', {
        'form': form,
        'title': 'Receive Inventory Stock'
    })

# --- PAGE VIEWS ---

def index(request):
    return render(request,'index.html')

def inventory(request):
    all_spare_parts = SparePart.objects.all()
    all_invoices = InventoryInvoice.objects.all()
    context = {
        'spare_parts': all_spare_parts,
        'inventory_invoices': all_invoices,
    }
    return render(request,'inventory.html', context)

def customers(request):
    all_customers = Customer.objects.all()
    all_vehicles = Vehicle.objects.all() 
    context = {
        'customers': all_customers,
        'vehicles': all_vehicles,
    }
    return render(request,'customers.html', context)

def employee(request):
    all_employees = Employee.objects.all()
    context = {
        'employees': all_employees,
    }
    return render(request,'employee.html', context)

def profile(request):
    return render(request,'profile.html')

def services(request):
    all_records = Service.objects.all() 
    all_invoices = ServiceInvoice.objects.all()
    context = {
        'service_records': all_records,
        'service_invoices': all_invoices,
    }
    return render(request,'services.html', context)


# --- FORM VIEWS FOR SERVICES PAGE (FIXED) ---

@xframe_options_sameorigin
def service_record_create(request):
    # This is a placeholder. You need to create 'ServiceRecordForm'
    # and the corresponding template.
    if request.method == 'POST':
        # form = ServiceRecordForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return render(request, 'services/service_record_done.html')
        pass
    else:
        # form = ServiceRecordForm()
        pass
    
    # We are returning a placeholder for now
    # You should create 'services/service_form_base.html'
    # and 'ServiceRecordForm' in forms.py
    
    # FOR NOW, let's use a generic template to stop the crash:
    form = SparePartForm() # Using a spare part form as a temporary placeholder
    return render(request, 'inventory/inventory_form_base.html', {
        'form': form,
        'title': 'Create New Service Record (Placeholder)'
    })

@xframe_options_sameorigin
def service_invoice_create(request):
    # This is a placeholder. You need to create 'ServiceInvoiceForm'
    # and the corresponding template.
    if request.method == 'POST':
        # form = ServiceInvoiceForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return render(request, 'services/service_invoice_done.html')
        pass
    else:
        # form = ServiceInvoiceForm()
        pass

    # FOR NOW, let's use a generic template to stop the crash:
    form = InventoryInvoiceForm() # Using an invoice form as a temporary placeholder
    return render(request, 'inventory/inventory_form_base.html', {
        'form': form,
        'title': 'Create New Service Invoice (Placeholder)'
    })