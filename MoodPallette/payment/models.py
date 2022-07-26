from django.db import models

# Create your models here.
class payment(models.Model):
    pay_price = models.IntegerField()
    pay_date = models.DateField()
    pay_method = models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.id