from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django_mysql.models import ListCharField
from django.db.models import CharField
# Create your models here.

class profiles(models.Model):# change the model name as userProfile and goto update profile after signup
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(default="Name" ,blank=True,max_length=200, null=True)
    surname = models.CharField(default="Surname",blank=True, max_length=200, null=True)
    phn = models.CharField(default="Phone number",blank=True,max_length=200,null=True)
    email =  models.CharField(default="Email",blank=True,max_length=200,null=True)
    address = models.CharField(default="Address",blank=True,max_length=50,null=True)
    education = models.CharField(default="education",blank=True,max_length=50,null=True)
    country = models.CharField(default="country",blank=True,max_length=50,null=True)
    state = models.CharField(default="state",blank=True,max_length=50,null=True)
    profile_pic = models.ImageField(default="profile2.png" ,blank=True, null=True , upload_to='user/')
    experience = models.CharField(default="Experience",blank=True,null=True, max_length=300)
    additionaldetails = models.CharField(default="Additional details",blank=True,null=True, max_length=300)
    sublist = ListCharField(base_field=CharField(max_length=20),size=5,max_length=(5 * 21))
    
    def __str__(self):
        return str(self.user)


def create_profile(sender, instance, created, **kwargs):

    if created:
        profiles.objects.create(user = instance)

post_save.connect(create_profile , sender=User)


def update_profile(sender, instance, **kwargs):
    instance.profiles.save()

post_save.connect(update_profile , sender=User)

class subbrand(models.Model):   #remove this and use from brand app model(Brand)
    # # bname = models.CharField(blank=True,max_length=200, null=True)
    # # bpic = models.ImageField(blank=True, null=True)
    def __str__(self):
        return str(self.bname)


        

