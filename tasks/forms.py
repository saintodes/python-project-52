from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext

from labels.models import Labels
from .models import Tasks
from statuses.models import Status


class CreateTaskForm(forms.ModelForm):
    class Meta:

        model = Tasks
        fields = ['name', 'description', 'status', 'executor_id', 'label']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': gettext('Name')}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': gettext('Description')}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'executor_id': forms.Select(attrs={'class': 'form-select'}),
            'label': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) > 150:
            raise ValidationError(gettext("Task length cannot exceed 150 characters."))
        return name

    def save(self, commit=True, *args, **kwargs):
        task = super(CreateTaskForm, self).save(commit=False, *args, **kwargs)
        if not task.executor_id:
            task.executor_id = task.author_id
        if commit:
            task.save()
            self.save_m2m()
        return task
