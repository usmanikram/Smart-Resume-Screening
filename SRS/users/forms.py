from django.forms import ModelForm
from base.models import Job,Resume
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ClearableFileInput


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

