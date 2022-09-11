from enum import unique
from django.db import models

from account.models import User


# Create your models here.

class Prodcut_categories(models.Model):
    name = models.CharField(max_length=100, blank=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    # img = models.ImageField(upload_to=None, max_length=100, null=True, blank=True)
    category = models.ForeignKey(Prodcut_categories, blank=True, null=True,on_delete=models.CASCADE)

class Cart(models.Model): 
    user = models.ForeignKey(User ,on_delete=models.CASCADE)    
    on_create = models.DateTimeField(auto_now_add=True)

class ProductInCart(models.Model):
    class Meta:
        unique_together = (("cart", "product"),)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()    

class Order (models.Model):
    status_choices = (
        (1,"Not Packed"),
        (2,"Ready To Shipment"),
        (3,"Shipped"),
        (4,"Out For Delivery"),
        (5,"Delivered")
        )
    user = models.ForeignKey(User ,on_delete=models.CASCADE)    
    status = models.IntegerField(choices=status_choices, default=1)
    