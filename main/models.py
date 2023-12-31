# Create your models here.
from django.db import models
from django.utils.timezone import *
from django.contrib.auth.models import User
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # nama produk
    amount = models.IntegerField(default=0) # dalam lusin
    price = models.IntegerField(default=0) # dalam rupiah
    description = models.TextField(default="") # Nama PT yang supply
    date_in = models.DateField(auto_now_add=True)
    stock = models.BooleanField(default=0)
    categories = models.CharField(max_length=100, default='uncategorized')

    
