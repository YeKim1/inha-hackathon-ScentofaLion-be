from tkinter import CASCADE
from django.db import models
from product.models import product

class subSet(models.Model):
    color = models.CharField(max_length=6, default="")
    count = models.IntegerField(default=0)
    diffuser = models.ForeignKey(product, on_delete=models.CASCADE, null=True, related_name="diffuser")
    handwash = models.ForeignKey(product, on_delete=models.CASCADE, null=True, related_name="handwash")
    handcream = models.ForeignKey(product, on_delete=models.CASCADE, null=True, related_name="handcream")
    softner = models.ForeignKey(product, on_delete=models.CASCADE, null=True, related_name="softner")
    perfume = models.ForeignKey(product, on_delete=models.CASCADE, null=True, related_name="perfume")
    shampoo = models.ForeignKey(product, on_delete=models.CASCADE, null=True, related_name="shampoo")
    rinse = models.ForeignKey(product, on_delete=models.CASCADE, null=True, related_name="rinse")
    bodywash = models.ForeignKey(product, on_delete=models.CASCADE, null=True, related_name="bodywash")
    candle = models.ForeignKey(product, on_delete=models.CASCADE, null=True, related_name="candle")
    room = models.ForeignKey(product, on_delete=models.CASCADE, null=True, related_name="room")
    bodymist = models.ForeignKey(product, on_delete=models.CASCADE, null=True, related_name="bodymist")
    bodylotion = models.ForeignKey(product, on_delete=models.CASCADE, null=True, related_name="bodylotion")

