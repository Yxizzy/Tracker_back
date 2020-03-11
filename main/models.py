from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tracker(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Product(models.Model):
    vendor = (
        ("Jumia", "Jumia"),
        ("Konga", "Konga"),
        ("Yudala", "Yudala"),
        ("Ebay", "Ebay")
    )
    status = (
        ("Order Confirmed", "Order Confirmed"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered")
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    vendor = models.CharField(max_length=50, choices=vendor, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=50, choices=status, null=True, blank=True)
    code = models.ForeignKey(Tracker, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, null=True, blank=True)

class Status(models.Model):
    id =models.AutoField(primary_key=True)
    status = models.CharField(max_length=500, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True, null=True, blank=True)