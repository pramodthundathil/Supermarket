from django.db import models
from products.models import Products
from django.contrib.auth.models import User

# Create your models here.

class BillCalculations(models.Model):
    
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.CharField(max_length=11)
    gst = models.CharField(max_length=100,null=True)
    totalprice = models.CharField(max_length=100,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    
class Cart(models.Model):
    
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    itemcount = models.CharField(max_length=255)
    
class CheckoutBill(models.Model):
    
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    
class DeliveryAddress(models.Model):
    
    Name = models.CharField(max_length=255)
    phone = models.IntegerField()
    house = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)  
    
class BillId(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    itemquantity = models.CharField(max_length=255)
    totalprice = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    status = models.BooleanField(default=True)
    
class SaleBill(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    Billid = models.ForeignKey(BillId,on_delete=models.CASCADE)  
    
    