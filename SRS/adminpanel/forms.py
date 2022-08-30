from django.forms import ModelForm
from base.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ClearableFileInput

class addUserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ('last_login','is_staff','is_active',)
