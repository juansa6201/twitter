# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
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
    username = forms.CharField(label='Nombre de usuario', max_length=30, required=False, help_text='Obligatorio. Solo puede estar formado por letras, números y los caracteres @/./+/-/_..')
    first_name = forms.CharField(label='Nombre', max_length=30, required=False, help_text='Opcional.')
    last_name = forms.CharField(label='Apellido', max_length=30, required=False, help_text='Opcional.')
    email = forms.EmailField(max_length=254, help_text='Obligatorio.')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(), help_text='Introduce una contraseña')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
