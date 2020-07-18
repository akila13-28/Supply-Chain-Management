from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import designerProfile
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']
        
class ProfilesForm(forms.ModelForm):
    class Meta:
        model = designerProfile
        fields = '__all__'
        #fields=['user', 'name', 'phn', 'address', 'email', 'education', 'country', 'state', 'profile_pic']
        # exclude = ['user']