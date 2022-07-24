from django.db import models

# Create your models here.
class product(models.Model):
    product_name = models.CharField(max_length=100)
    product_color = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    product_img = models.ImageField()

    def __str__(self):
        return self.product_name