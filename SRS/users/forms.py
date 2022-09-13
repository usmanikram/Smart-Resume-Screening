from django.forms import ModelForm
from base.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ClearableFileInput


class CreateJobForm(ModelForm):
    class Meta:
        model = Job
        exclude = ('user_id','completion_date',)

class CreateJobFormForResume(ModelForm):
    class Meta:
        model = Resume
        exclude = ('job_id',)
        widgets = {
            'resume': ClearableFileInput(attrs={'multiple': True}),
        }


class EditUserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ('last_login','is_approved','is_staff','is_active',)


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        exclude = ('job_id','title',)