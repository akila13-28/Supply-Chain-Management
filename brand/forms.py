from django.forms import ModelForm
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