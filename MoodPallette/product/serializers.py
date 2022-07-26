from rest_framework import serializers
from .models import product, color

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ('product_name', 'product_color', 'product_type', 'product_img')

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = color
        fields = ('color_name', 'color_keyword1', 'color_keyword2', 'color_keyword3', 'color_img')
