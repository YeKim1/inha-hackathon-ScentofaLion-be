from rest_framework import serializers
from .models import product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ('product_name', 'product_color', 'product_type', 'product_img')
