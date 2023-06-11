from django import forms
from django.contrib.auth.models import User

from . import models


class ProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['name', 'surname', 'email_address']


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput
        }
