from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext

from .models import Tasks


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['name', 'description', 'status', 'executor', 'labels']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': gettext('Name')}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': gettext('Description')}),
            'status': forms.Select(
                attrs={'class': 'form-select'}),
            'executor': forms.Select(
                attrs={'class': 'form-select'}),
            'labels': forms.SelectMultiple(
                attrs={'class': 'form-select'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) > 150:
            raise ValidationError(gettext("Task length cannot exceed 150 characters."))
        return name
