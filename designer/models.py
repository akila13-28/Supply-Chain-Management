from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class designerProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=200, null=True)
    LastName = models.CharField(max_length=200, null=True)
#     DOB = models.DateTimeField(null=True)
#     Mobile = models.CharField(max_length=200,null=True)
#     Category = models.CharField(max_length=200,null=True)
#     email = models.EmailField(max_length=50,null=True)
#     country = models.CharField(max_length=50,null=True)
#     state = models.CharField(max_length=50,null=True)
#  #   profile_pic = models.ImageField(null=True, blank=True)
#     About = models.CharField(max_length=200,null=True)
    def __str__(self):
        return str(self.user)