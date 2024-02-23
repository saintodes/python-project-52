from django import forms
from django.utils.translation import gettext

from .models import Status


class CreateStatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': gettext('Name')}),
            }
        labels = {
            'name': gettext('Name'),
            }
