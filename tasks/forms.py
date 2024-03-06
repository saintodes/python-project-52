from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext

from .models import Tasks
from statuses.models import Status


class CreateTaskForm(forms.ModelForm):
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        empty_label='----------',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    performer_user_id = forms.ModelChoiceField(
        queryset=get_user_model().objects.all(),
        empty_label='---------',
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    class Meta:
        model = Tasks
        fields = ['name', 'description', 'status', 'performer_user_id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': gettext('Name')}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': gettext('Description')}),
        }
        labels = {
            'name': gettext('Name'),
            'description': gettext('Description'),
            'status': gettext('Status'),
            'performer_user_id': gettext('Performer'),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) > 150:
            raise ValidationError(gettext("Task length cannot exceed 150 characters."))
        return name



    def save(self, commit=True, *args, **kwargs):
        task = super(CreateTaskForm, self).save(commit=False, *args, **kwargs)
        if not task.performer_user_id:
            task.performer_user_id = task.created_by_user_id
        if commit:
            task.save()
        return task
