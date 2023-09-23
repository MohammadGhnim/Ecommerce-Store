from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class SignupForm():
    class Meta:
        Model = User
        fields = ['username', 'email', 'password1', 'password2']


class ActivateUser(forms.Form):
    code=forms.CharField(max_length=8)