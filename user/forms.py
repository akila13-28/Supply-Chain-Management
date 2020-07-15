
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import profiles
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']
        
class ProfilesForm(forms.ModelForm):
    class Meta:
        model = profiles
        fields = '__all__'
        #fields=['user', 'name', 'phn', 'address', 'email', 'education', 'country', 'state', 'profile_pic']
        exclude = ['user']