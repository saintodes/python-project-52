from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
import re


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Login", widget=forms.TextInput(attrs={'class': 'form-control'}),
                               help_text="Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', "autocomplete": "new-password"}),
                                help_text='Ваш пароль должен содержать как минимум 3 символа.')
    password2 = forms.CharField(label="Password repeat", widget=forms.PasswordInput(
        attrs={'class': 'form-control', "autocomplete": "new-password"}),
                                help_text='Для подтверждения введите, пожалуйста, пароль ещё раз.')

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
        labels = {
            'first_name': "First name",
            'last_name': "Last name",
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 3:
            raise ValidationError("Ваш пароль должен содержать как минимум 3 символа.")
        return password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) > 150:
            raise ValidationError("Имя пользователя не может быть более 150 символов.")
        if not re.match(r'^[\w.@+-]+$', username):
            raise ValidationError("Имя пользователя может содержать только буквы, цифры и символы @/./+/-/_.")
        return username
