from django.forms import ModelForm
from django import forms
from .models import User,Job,Resume
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ClearableFileInput

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ('last_login','is_approved','is_staff','is_active',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Signup'))


class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput,
            'email': forms.EmailInput,
            'contact': forms.NumberInput,
            'company_contact': forms.NumberInput,
        }
        exclude = ('last_login','is_approved','is_staff','is_active',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Signup'))




class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('email','password')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Sign In'))


class CreateJobForm(ModelForm):
    class Meta:
        model = Job
        exclude = ('completion_date',)

class CreateJobFormForResume(ModelForm):
    class Meta:
        model = Resume
        exclude = ('job_id',)
        widgets = {
            'file_path': ClearableFileInput(attrs={'multiple': True}),
        }

