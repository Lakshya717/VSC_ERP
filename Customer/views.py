from formtools.wizard.views import SessionWizardView
from django.shortcuts import render
from .forms import UserCreateForm, CustomerForm
from .models import User

FORMS = [
    ("user", UserCreateForm),
    ("customer", CustomerForm),
]

TEMPLATES = {
    "user": "customer/wizards/customer_step_user.html",
    "customer": "customer/wizards/customer_step_details.html",
}

class CustomerCreationWizard(SessionWizardView):
    form_list = FORMS
    
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

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