from django import forms
from .models import *

class AddRegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['master', 'service', 'reg_date', 'reg_time', 'users_name', 'phone_number']
        widgets = {
            'service': forms.CheckboxSelectMultiple,
            'reg_date': forms.SplitDateTimeWidget,
            'reg_time': forms.DateTimeInput
        }