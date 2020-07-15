from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#instead RegisterPage create as in User app

class Registerpage(models.Model):
    bid= models.IntegerField(null=True)
    bname = models.CharField(max_length=40, null=True)
    bemail = models.CharField(max_length=40, null=True)
    password = models.CharField(max_length=40, null=True)
    logo = models.ImageField(null=True, blank=True,upload_to='brand/')
    certificate = models.CharField(max_length=40, null=True,blank=True)
    web = models.URLField(max_length=100,null= True, blank=True)

    
    def __str__(self):
        return self.bname
    
#//////needed      
# class Brand(models.Model):
#     id = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     bname = models.CharField(max_length=40, null=True)
#     bemail = models.CharField(max_length=40, null=True)
#     bpic = models.ImageField(null=True, blank=True)
#     certificate = models.CharField(max_length=40, null=True,blank=True)
#     web = models.URLField(max_length=100,null= True, blank=True)  
#     def __str__(self):
#         return self.bname




class Product(models.Model):
    CATEGORY =(
        ('mens','mens'),
        ('womens','womens'),
        ('kids-boys','kids-boys'),
        ('kids-girls','kids-girls')
    )
    brand= models.ForeignKey(Registerpage,null=True, on_delete=models.CASCADE)
#   brand= models.CharField(max_length=40, null=True)
    name = models.CharField(max_length=40, null=True)
    designer = models.CharField(max_length=40, null=True)
    ratings = models.CharField(max_length=40, null=True)
    quantity = models.CharField(max_length=40,null=True)
    price = models.CharField(max_length=40,null=True)
    images = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=250,null=True)
    category = models.CharField(max_length=40,null=True,choices=CATEGORY)
    date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    size = models.CharField(max_length=40,null=True)


    def __str__(self):
        return self.name

#delete this and use from designer model.py
class Designer(models.Model):
    # name = models.CharField(max_length=100,null= True, blank=True)
    # designation = models.CharField(max_length=100,null= True, blank=True)
    # email = models.CharField(max_length=100,null= True, blank=True)
    # phone = models.CharField(max_length=10, null= True, blank=True)
    # images = models.ImageField(null=True, blank=True)
    # facebook = models.URLField(max_length=100,null= True, blank=True)
    # insta = models.URLField(max_length=100,null= True, blank=True)

    def __str__(self):
        return self.name



class challenges(models.Model):
    # name= models.ForeignKey(Brand,null=True, on_delete=models.CASCADE)
    cname=models.CharField(max_length=30)
    cdesc=models.TextField()
    csme=models.IntegerField()
    cparticipants=models.IntegerField()
    cdesigners=models.IntegerField()
    cdobegin=models.DateField()
    
    def __str__(self):
        return self.cname




