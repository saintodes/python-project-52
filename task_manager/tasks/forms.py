from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext
from django.contrib.auth import get_user_model

from .models import Tasks


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['name', 'description', 'status', 'executor', 'label']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': gettext('Name')}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': gettext('Description')}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'executor': forms.Select(attrs={'class': 'form-select'}),
            'label': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super(CreateTaskForm, self).__init__(*args, **kwargs)
        self.fields['executor'].queryset = get_user_model().objects.all()
        self.fields['executor'].label_from_instance = self.format_executor_label

    @staticmethod
    def format_executor_label(obj):
        return f"{obj.first_name} {obj.last_name}"

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) > 150:
            raise ValidationError(gettext("Task length cannot exceed 150 characters."))
        return name
