from django.db import models
from subSelect.models import subSelect

# Create your models here.
class subSet(models.Model):
    color = models.CharField(max_length=6, default="")
    subSelect_id = models.ForeignKey(subSelect, on_delete=models.PROTECT, db_column="subSelect_id", null=True)
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