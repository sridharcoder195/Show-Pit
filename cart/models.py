from django.db import models
from shop.models import *


# Create your models here.
class cart(models.Model):
    cart_id = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class catitems(models.Model):
    prodt = models.ForeignKey(Products, on_delete=models.CASCADE)
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    quan = models.IntegerField()

    def __str__(self):
        return self.prodt

    def total(self):
        return self.prodt.price * self.quan
