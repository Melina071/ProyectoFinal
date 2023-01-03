from django import forms
from AppArte.models import *
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

class formLibros(forms.Form):

    nombre=forms.CharField(max_length=70)
    autor=forms.CharField(max_length=70)
    año=forms.IntegerField(min_value=1900, max_value=2023, widget=forms.NumberInput)
    genero=forms.CharField(max_length=70)    
    puntaje= forms.FloatField(min_value=0, max_value=10)
    descripcion= forms.CharField(widget=forms.Textarea())
    portada= forms.ImageField()

class formDiscos(forms.Form):

    nombre=forms.CharField(max_length=70)
    artista=forms.CharField(max_length=70)
    año=forms.IntegerField(min_value=1900, max_value=2023)
    genero=forms.CharField(max_length=70)    
    puntaje= forms.FloatField(min_value=0, max_value=10)
    descripcion= forms.CharField(widget=forms.Textarea())
    tapa= forms.ImageField(required=False)


class formPinturas(forms.Form):
    
    nombre=forms.CharField(max_length=70)
    artista=forms.CharField(max_length=70)
    año=forms.IntegerField(min_value=1900, max_value=2023)
    descripcion= forms.CharField(widget=forms.Textarea())    
    foto= forms.ImageField()

class registroUsuario(UserCreationForm):
    
    email=forms.EmailField()
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)
    
    class Meta:
        
        model= User
        fields=["username", "email", "first_name", "last_name", "password1", "password2"]
        
class editarUserForm(UserCreationForm):
    
    email=forms.EmailField()
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)
    
    class Meta:
        
        model= User
        fields=['email', 'first_name', 'last_name', 'password1', 'password2']
        

class avatarForm(forms.ModelForm):
    
    class Meta:
        
        model= Avatar
        fields= ["imagen"]    