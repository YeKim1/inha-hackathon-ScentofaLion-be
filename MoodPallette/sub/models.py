from django.db import models

class subSelect(models.Model):
    diffuser_yn = models.BooleanField(default=False)
    handwash_yn = models.BooleanField(default=False)
    handcream_yn = models.BooleanField(default=False)
    sofrner_yn = models.BooleanField(default=False)
    perfume_yn = models.BooleanField(default=False)
    shampoo_yn = models.BooleanField(default=False)
    rinse_yn = models.BooleanField(default=False)
    bodywash_yn = models.BooleanField(default=False)
    candle_yn = models.BooleanField(default=False)
    room_yn = models.BooleanField(default=False)
    diffuser_yn = models.BooleanField(default=False)
    diffuser_yn = models.BooleanField(default=False)


class subSet(models.Model):
    color = models.CharField(max_length=6, default="")
    subSelect_id = models.IntegerField()
    diffuser_name = models.CharField(max_length=100, default="")
    handwash_name = models.CharField(max_length=100, default="")
    handcream_name = models.CharField(max_length=100, default="")
    sofrner_name = models.CharField(max_length=100, default="")
    perfume_name = models.CharField(max_length=100, default="")
    shampoo_name = models.CharField(max_length=100, default="")
    rinse_name = models.CharField(max_length=100, default="")
    bodywash_name = models.CharField(max_length=100, default="")
    candle_name = models.CharField(max_length=100, default="")
    room_name = models.CharField(max_length=100, default="")
    bodymist_name = models.CharField(max_length=100, default="")
    bodylotion_name = models.CharField(max_length=100, default="")

