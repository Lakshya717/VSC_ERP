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
from django.db.models import ProtectedError

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
            return render(request, 'customer/wizards/vehicle_form_done.html')
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
    parts_qs = SparePart.objects.select_related('vehicle_model', 'type').all()
    invoices_qs = InventoryInvoice.objects.select_related('spare_part').all()

    spare_part_filter = SparePartFilter(request.GET, queryset=parts_qs, prefix='parts')
    inventory_invoice_filter = InventoryInvoiceFilter(request.GET, queryset=invoices_qs, prefix='inv')

    context = {
        'spare_parts': spare_part_filter.qs,
        'spare_part_filter': spare_part_filter,
        'is_filtered_spare_parts': bool(spare_part_filter.form.changed_data),

        'inventory_invoices': inventory_invoice_filter.qs,
        'inventory_invoice_filter': inventory_invoice_filter,
        'is_filtered_inventory_invoices': bool(inventory_invoice_filter.form.changed_data),
    }
    return render(request,'inventory.html', context)

@login_required()
def customers(request):
    # ... (rest of view) ...
    all_customers = Customer.objects.select_related('user').all()
    all_vehicles = Vehicle.objects.select_related('customer__user', 'model__brand').all() 
    customer_filter = CustomerFilter(request.GET, queryset=all_customers, prefix='cust')
    vehicle_filter = VehicleFilter(request.GET, queryset=all_vehicles, prefix='veh')
    context = {
        'customers': customer_filter.qs,
        'customer_filter': customer_filter,
        'is_filtered_customers': bool(customer_filter.form.changed_data),
        'vehicles': vehicle_filter.qs,
        'vehicle_filter': vehicle_filter,
        'is_filtered_vehicles': bool(vehicle_filter.form.changed_data),
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
@require_POST
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    try:
        display_name = customer.user.get_full_name() or customer.user.username
        customer.delete()
        messages.success(request, f"Customer '{display_name}' has been deleted.")
    except ProtectedError:
        messages.error(request, "Cannot delete customer because related vehicles or services exist.")
    return redirect('CORE:customers')


@login_required
@require_POST
def vehicle_delete(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    try:
        reg = vehicle.registration_number
        vehicle.delete()
        messages.success(request, f"Vehicle '{reg}' has been deleted.")
    except ProtectedError:
        messages.error(request, "Cannot delete vehicle because related service records exist.")
    return redirect('CORE:customers')


@login_required
@require_POST
def spare_part_delete(request, pk):
    part = get_object_or_404(SparePart, pk=pk)
    try:
        name = part.name
        part.delete()
        messages.success(request, f"Spare part '{name}' has been deleted.")
    except ProtectedError:
        messages.error(request, "Cannot delete spare part because invoices or service usages exist.")
    return redirect('CORE:inventory')


@login_required
@require_POST
def inventory_invoice_delete(request, pk):
    invoice = get_object_or_404(InventoryInvoice, pk=pk)
    try:
        invoice_id = invoice.id
        invoice.delete()
        messages.success(request, f"Inventory invoice '{invoice_id}' has been deleted and stock adjusted.")
    except Exception:
        messages.error(request, "Failed to delete inventory invoice.")
    return redirect('CORE:inventory')


@login_required
@require_POST
def service_delete(request, pk):
    svc = get_object_or_404(Service, pk=pk)
    try:
        sid = svc.id
        svc.delete()
        messages.success(request, f"Service record '{sid}' has been deleted.")
    except ProtectedError:
        messages.error(request, "Cannot delete service record because an invoice exists.")
    return redirect('CORE:services')


@login_required
@require_POST
def service_invoice_cancel(request, pk):
    inv = get_object_or_404(ServiceInvoice, pk=pk)
    if inv.status == 'CANCELLED':
        messages.info(request, f"Service invoice '{inv.id}' is already cancelled.")
    else:
        inv.status = 'CANCELLED'
        inv.save()
        messages.success(request, f"Service invoice '{inv.id}' has been cancelled.")
    return redirect('CORE:services')

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
    records_qs = Service.objects.select_related('customer__user', 'vehicle', 'mechanic__employee__user').all() 
    invoices_qs = ServiceInvoice.objects.select_related('service__customer__user').all()

    service_filter = ServiceFilter(request.GET, queryset=records_qs, prefix='svc')
    service_invoice_filter = ServiceInvoiceFilter(request.GET, queryset=invoices_qs, prefix='svcinv')

    context = {
        'service_records': service_filter.qs,
        'service_filter': service_filter,
        'is_filtered_service_records': bool(service_filter.form.changed_data),

        'service_invoices': service_invoice_filter.qs,
        'service_invoice_filter': service_invoice_filter,
        'is_filtered_service_invoices': bool(service_invoice_filter.form.changed_data),
        'service_status_choices': Service._meta.get_field('status').choices,
        'service_invoice_status_choices': ServiceInvoice._meta.get_field('status').choices,
    }
    return render(request,'services.html', context)


@login_required
@require_POST
def service_status_update(request, pk):
    svc = get_object_or_404(Service, pk=pk)
    new_status = request.POST.get('status')
    valid_choices = {value for value, _ in Service._meta.get_field('status').choices}

    if new_status not in valid_choices:
        messages.error(request, "Invalid status selection.")
        return redirect('CORE:services')

    # If an invoice exists, lock status to BILLED or CANCELLED only as per business rule
    if hasattr(svc, 'invoice') and svc.invoice is not None:
        if new_status != 'BILLED' and new_status != 'CANCELLED':
            messages.error(request, "Cannot change status of a billed service to a non-billed state.")
            return redirect('CORE:services')

    svc.status = new_status
    svc.save(update_fields=['status'])
    messages.success(request, f"Service #{svc.id} status updated to '{dict(Service._meta.get_field('status').choices).get(new_status, new_status)}'.")
    return redirect('CORE:services')


@login_required
@require_POST
def service_invoice_status_update(request, pk):
    inv = get_object_or_404(ServiceInvoice, pk=pk)
    new_status = request.POST.get('status')
    valid_choices = {value for value, _ in ServiceInvoice._meta.get_field('status').choices}

    if new_status not in valid_choices:
        messages.error(request, "Invalid invoice status selection.")
        return redirect('CORE:services')

    # Optional rule: prevent changing a CANCELLED invoice back to active states
    if inv.status == 'CANCELLED' and new_status != 'CANCELLED':
        messages.error(request, "Cannot change a cancelled invoice.")
        return redirect('CORE:services')

    inv.status = new_status
    inv.save(update_fields=['status'])
    messages.success(request, f"Service Invoice #{inv.id} status updated to '{dict(ServiceInvoice._meta.get_field('status').choices).get(new_status, new_status)}'.")
    return redirect('CORE:services')
