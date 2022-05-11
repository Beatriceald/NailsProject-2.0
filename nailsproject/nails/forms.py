from django import forms
from django.forms import ModelForm, MultipleChoiceField, SelectMultiple
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class AddRegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['master'].empty_label = "Мастер не выбран"

    class Meta:
        model = Registration
        fields = ['master', 'service', 'reg_date', 'reg_time', 'users_name', 'phone_number']
        service = MasterService.objects.all()
        widgets = {
            'reg_date': DateInput(),
            'reg_time': TimeInput(),
            'service': forms.CheckboxSelectMultiple
        }