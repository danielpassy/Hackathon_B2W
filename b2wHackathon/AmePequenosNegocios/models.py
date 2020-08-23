from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate, login, logout
from django.forms import ModelForm, FileInput, TextInput, DateInput, NumberInput

## GLOBALS VARIABLES,
DESCRIPTION_MAX_LENGHT = 500
CATEGORY_MAX_LENGHT = 80
MESSAGE_MAX_LENGHT = 500
NAME_MAX_LENGHT = 100

# Create your models here.

class User(AbstractUser):
    pass


class Product(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=NAME_MAX_LENGHT)
    timestamp = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(blank=False)
    cashback = models.FloatField()
    description = models.CharField(max_length=DESCRIPTION_MAX_LENGHT)
    active = models.BooleanField(default=True)
    image = models.FileField(upload_to='uploads/', blank=True)



class ProductImage(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="images")


class Category(models.Model):
    products = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='categorias')
    name = models.CharField(max_length=CATEGORY_MAX_LENGHT)


class Chat(models.Model):
    seller = models.ForeignKey('User', on_delete=models.CASCADE, related_name='msgSend')
    buyer = models.ForeignKey('User', on_delete=models.CASCADE, related_name='msgReceive')
    content = models.CharField(max_length=MESSAGE_MAX_LENGHT)
    timestamp = models.DateTimeField(auto_now_add=True)

class Transaction(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="transactions")
    seller = models.ForeignKey('User', on_delete=models.CASCADE, related_name='sellings')
    buyer = models.ForeignKey('User', on_delete=models.CASCADE, related_name='buyings')
    price = models.FloatField()
    cashback = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)