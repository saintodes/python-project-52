from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
import re
from django.utils.translation import gettext


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Login", widget=forms.TextInput(attrs={'class': 'form-control'}),
                               help_text=gettext(
                                   "Required field. No more than 150 characters. Only letters, numbers, and symbols. @/./+/-/_."))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', "autocomplete": "new-password"}),
                                help_text=gettext('Your password must contain at least 3 characters.'))
    password2 = forms.CharField(label="Password repeat", widget=forms.PasswordInput(
        attrs={'class': 'form-control', "autocomplete": "new-password"}),
                                help_text=gettext('Please enter your password again for confirmation.'))
    first_name = forms.CharField(label=gettext("First name"), widget=forms.TextInput(attrs={'class': 'form-control'}),
                                 required=True)
    last_name = forms.CharField(label=gettext("Last name"), widget=forms.TextInput(attrs={'class': 'form-control'}),
                                required=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 3:
            raise ValidationError(gettext("Your password must contain at least 3 characters."))
        return password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) > 150:
            raise ValidationError(gettext("The username length cannot exceed 150 characters."))
        if not re.match(r'^[\w.@+-]+$', username):
            raise ValidationError(gettext("The username can only contain letters, numbers, and the symbols @/./+/-/_."))
        return username
