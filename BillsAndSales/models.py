from django.db import models
from products.models import Products
from django.contrib.auth.models import User

# Create your models here.

class BillCalculations(models.Model):
    
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.CharField(max_length=11)
    gst = models.CharField(max_length=100,null=True)
    totalprice = models.CharField(max_length=100,null=True)
    
class Cart(models.Model):
    
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    itemcount = models.CharField(max_length=255)
    