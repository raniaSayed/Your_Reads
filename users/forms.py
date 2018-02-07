from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    username=forms.CharField(max_length = 100)
    class Meta:
        model=User
        fields=['username','email','password']

class UserFormLogin(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    username=forms.CharField(max_length = 100)
    class Meta:
        model=User
        fields=['username','password']
