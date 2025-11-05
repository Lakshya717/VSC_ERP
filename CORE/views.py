from formtools.wizard.views import SessionWizardView
from django.shortcuts import render
from django.forms import Form

from .forms import *
from .models import *

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

class EmployeeCreationWizard(SessionWizardView):
    form_list = [
        ("user", UserCreateForm),
        ("employee", EmployeeForm),
        ("role_details", Form), # Empty placeholder
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
                role = employee_data.get('role') # This is a MASTER_role instance
                
                if role.name == 'Mechanic':
                    self.form_list[step] = MechanicForm
                elif role.name == 'Accountant':
                    self.form_list[step] = AccountantForm
                elif role.name == 'Cashier':
                    self.form_list[step] = CashierForm
                elif role.name == 'Advisor':
                    self.form_list[step] = AdvisorForm
                else:
                    # For roles with no extra data (e.g., Janitor)
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

        # 3. Save Role-Specific Details (if the form wasn't empty)
        if not isinstance(role_form, Form):
            role_model = role_form.save(commit=False)
            
            role_model.employee = employee 
            role_model.save()
        
        return render(self.request, 'employee/wizards/employee_wizard_done.html', {
            'username': user.username
        })


def spare_part_create(request):
    if request.method == 'POST':
        form = SparePartForm(request.POST)
        if form.is_valid():
            part = form.save()
            # Send a success message back to the modal
            return render(request, 'inventory/inventory_part_done.html', {
                'part_name': part.name
            })
    else:
        form = SparePartForm()
    
    return render(request, 'inventory/inventory_form_base.html', {
        'form': form,
        'title': 'Add New Part to Catalog'
    })

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

def index(request):
    return render(request,'index.html')

def inventory(request):
    return render(request,'inventory.html')

def customers(request):
    return render(request,'customers.html')

def employee(request):
    return render(request,'employee.html')

def profile(request):
    return render(request,'profile.html')

def services(request):
    return render(request,'services.html')



