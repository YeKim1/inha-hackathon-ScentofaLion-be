from django.db import models

# Create your models here.
class product(models.Model):
    product_name = models.CharField(max_length=100, default="")
    product_color = models.CharField(max_length=100, default="")
    product_type = models.CharField(max_length=100, default="")
    product_img = models.ImageField(upload_to = 'product/')

    def __str__(self):
        return self.product_name

class color(models.Model):
    color_name = models.CharField(max_length=6, primary_key=True, unique=True)
    color_keyword1 = models.CharField(max_length=30)
    color_keyword2 = models.CharField(max_length=30)
    color_keyword3 = models.CharField(max_length=30)
    color_img = models.ImageField(upload_to = 'colorTheme/')

    def __str__(self):
        return self.color_name