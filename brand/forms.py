from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from .models import *

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields ='__all__'

class logs(ModelForm):
    class Meta:
        model = Registerpage
        fields = '__all__' 

class Design(ModelForm):
    class Meta:
        model = Designer
        fields = '__all__'

class BrandReg(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2']