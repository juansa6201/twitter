# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from models import *


class FormTweet(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('message',)
        widgets = {
            'message': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el mensaje'
            })
        }


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario', max_length=30, required=False, help_text='Obligatorio. Solo puede estar formado por letras, números y los caracteres @/./+/-/_..', widget=forms.TextInput(attrs={'class':'form-control'}))

    first_name = forms.CharField(label='Nombre', max_length=30, required=False, help_text='Opcional.',widget=forms.TextInput(attrs={'class':'form-control'}))

    last_name = forms.CharField(label='Apellido', max_length=30, required=False, help_text='Opcional.',widget=forms.TextInput(attrs={'class':'form-control'}))

    email = forms.EmailField(max_length=254, help_text='Obligatorio.',widget=forms.TextInput(attrs={'class':'form-control'}))

    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(), help_text='Introduce una contraseña')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

class MyLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder':'Username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'placeholder':'Password'}))


