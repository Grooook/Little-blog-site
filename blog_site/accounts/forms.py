from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
    attrs={'class':'form-control form-control-lg','type':'password', 'name': 'password1','placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
    attrs={'class':'form-control form-control-lg','type':'password', 'name': 'password2','placeholder':'Password confirmation'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'username' : forms.TextInput(
                attrs={
                    'class': 'form-control form-control-lg',
                    'placeholder':'Username'
                }
            ),
            'email' : forms.EmailInput(
                attrs={
                    'class': 'form-control form-control-lg',
                    'placeholder':'Email'
                }
            ),
        }


