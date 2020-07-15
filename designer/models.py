from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class designerProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    phn = models.CharField(max_length=200,null=True)
    email =  models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=50,null=True)
    education = models.CharField(max_length=50,null=True)
    country = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=50,null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    experience = models.CharField(null=True, max_length=300)
    additionaldetails = models.CharField(null=True, max_length=300)
    def __str__(self):
        return self.name