from django.db import models

# Create your models here.
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

    def __str__(self):
        return self.id