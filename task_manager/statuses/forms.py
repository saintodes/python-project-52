from django import forms
from django.core.exceptions import ValidationError
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

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) > 150:
            raise ValidationError(gettext("Status length cannot exceed 150 characters."))
        return name

