from tkinter import CASCADE
from django.db import models
from product.models import product

class subSet(models.Model):
    color = models.CharField(max_length=6, default="")
    price = models.IntegerField()
    date = models.DateField()
    diffuser = models.BooleanField(default=False)
    handwash = models.BooleanField(default=False)
    handcream = models.BooleanField(default=False)
    softner = models.BooleanField(default=False)
    perfume = models.BooleanField(default=False)
    shampoo = models.BooleanField(default=False)
    rinse = models.BooleanField(default=False)
    bodywash = models.BooleanField(default=False)
    candle = models.BooleanField(default=False)
    room = models.BooleanField(default=False)
    bodymist = models.BooleanField(default=False)
    bodylotion = models.BooleanField(default=False)

