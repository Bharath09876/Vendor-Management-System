from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class User_Detail(models.Model):
    name = models.CharField(max_length=20)
    Address = models.TextField(max_length=500)
    Phone_number = PhoneNumberField()
    Email = models.EmailField(max_length=254)
    image = models.ImageField(upload_to="static/user_images",default=None)