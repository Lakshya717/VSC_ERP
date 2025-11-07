from formtools.wizard.views import SessionWizardView
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.forms import Form
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm

from .forms import *
from .filters import *
from .models import *
from Masters.models import *

# ----------------- IFRAME VIEWS --------------------
@method_decorator(xframe_options_sameorigin, name='dispatch')
class CustomerCreationWizard(SessionWizardView):
    # ... (rest of class) ...
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
    # ... (rest of class) ...
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
    # ... (rest of view) ...
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
    # ... (rest of view) ...
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

@xframe_options_sameorigin
def vehicle_create(request):
    """
    Handles the creation of a new Vehicle.
    """
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'customers/vehicle_form_done.html')
    else:
        form = VehicleForm()
    
    # We can reuse the generic form template
    return render(request, 'services/service_form_base.html', {
        'form': form,
        'title': 'Add New Vehicle'
    })


# --- FORM VIEWS FOR SERVICES PAGE ---
@xframe_options_sameorigin
def service_record_create(request):
    # ... (rest of view) ...
    if request.method == 'POST':
        form = ServiceRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'services/service_record_done.html')
    else:
        form = ServiceRecordForm()
    
    return render(request, 'services/service_form_base.html', {
        'form': form,
        'title': 'Create New Service Record'
    })

@xframe_options_sameorigin
def service_invoice_create(request):
    # ... (rest of view) ...
    if request.method == 'POST':
        form = ServiceInvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'services/service_invoice_done.html')
    else:
        form = ServiceInvoiceForm()
    
    return render(request, 'services/service_form_base.html', {
        'form': form,
        'title': 'Create New Service Invoice'
    })

# ----------------- PAGE VIEWS --------------------
class login(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True

def logout(request):
    return logout_then_login(request,login_url= reverse('CORE:login'))

@login_required()
def index(request):
    return render(request,'index.html')

@login_required()
def inventory(request):
    all_spare_parts = SparePart.objects.all()
    all_invoices = InventoryInvoice.objects.all()
    context = {
        'spare_parts': all_spare_parts,
        'inventory_invoices': all_invoices,
    }
    return render(request,'inventory.html', context)

@login_required()
def customers(request):
    # ... (rest of view) ...
    all_customers = Customer.objects.all()
    all_vehicles = Vehicle.objects.all() 
    context = {
        'customers': all_customers,
        'vehicles': all_vehicles,
    }
    return render(request,'customers.html', context)

@login_required()
def employee(request):

    employee_list = Employee.objects.all()
    employee_filter = EmployeeFilter(request.GET, queryset=employee_list)
    is_filtered = bool(employee_filter.form.changed_data)

    context = {
        'employees': employee_filter.qs,
        'employee_filter': employee_filter,
        'is_filtered': is_filtered,
    }
    return render(request, 'employee.html', context)

@login_required
@require_POST
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)    
    user_full_name = employee.user.get_full_name() or employee.user.username
    employee.delete()
    messages.success(request, f"Employee '{user_full_name}' has been deleted.")
    return redirect('CORE:employee')

@login_required
def profile(request):
    user = request.user
    
    try:
        employee = user.Employee
    except Employee.DoesNotExist:
        employee = None
    
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'user_edit_form':
            user_form = UserProfileForm(request.POST, instance=user)
            employee_form = EmployeeProfileForm(instance=employee) if employee else None
            
            if user_form.is_valid():
                user_form.save()
                messages.success(request, "Profile updated successfully.")
                return redirect('CORE:profile')
            else:
                messages.error(request, "Please correct the profile errors.")

        elif form_type == 'employee_edit_form' and employee:
            employee_form = EmployeeProfileForm(request.POST, instance=employee)
            user_form = UserProfileForm(instance=user) 
            
            if employee_form.is_valid():
                employee_form.save()
                messages.success(request, "Employee details updated successfully.")
                return redirect('CORE:profile')
            else:
                messages.error(request, "Please correct the employee details errors.")
        
        elif form_type == 'employee_edit_form' and not employee:
            messages.error(request, "Cannot update: Employee profile not found.")
            user_form = UserProfileForm(instance=user)
            employee_form = None
            
    else:
        user_form = UserProfileForm(instance=user)
        employee_form = EmployeeProfileForm(instance=employee) if employee else None

    context = {
        'user_form': user_form,
        'employee_form': employee_form,
        'employee': employee
    }
    return render(request, 'profile.html', context)


@login_required()
def services(request):
    # ... (rest of view) ...
    all_records = Service.objects.all() 
    all_invoices = ServiceInvoice.objects.all()
    context = {
        'service_records': all_records,
        'service_invoices': all_invoices,
    }
    return render(request,'services.html', context)
