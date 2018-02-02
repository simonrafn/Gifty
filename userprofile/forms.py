from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class CustomUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', )
        error_css_class = 'error'
