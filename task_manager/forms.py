from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext as _
from django.utils.translation import pgettext


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label=pgettext("users_form", "Login"),
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
