from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
import re
from django.utils.translation import gettext as _


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label=_("Login"), widget=forms.TextInput(attrs={'class': 'form-control'}),
                               help_text=_(
                                   "Required field. No more than 150 characters. Only letters, numbers, and symbols. @/./+/-/_."))
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput(
        attrs={'class': 'form-control', "autocomplete": "new-password"}),
                                help_text=_('Your password must contain at least 3 characters.'))
    password2 = forms.CharField(label=_("Password repeat"), widget=forms.PasswordInput(
        attrs={'class': 'form-control', "autocomplete": "new-password"}),
                                help_text=_('Please enter your password again for confirmation.'))
    first_name = forms.CharField(label=_("First name"), widget=forms.TextInput(attrs={'class': 'form-control'}),
                                 required=True)
    last_name = forms.CharField(label=_("Last name"), widget=forms.TextInput(attrs={'class': 'form-control'}),
                                required=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 3:
            raise ValidationError(_("Your password must contain at least 3 characters."))
        return password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) > 150:
            raise ValidationError(_("The username length cannot exceed 150 characters."))
        if not re.match(r'^[\w.@+-]+$', username):
            raise ValidationError(_("The username can only contain letters, numbers, and the symbols @/./+/-/_."))
        return username
