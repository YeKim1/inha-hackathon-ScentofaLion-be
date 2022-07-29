from rest_framework import serializers
from .models import subSet

class subSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = subSet
        fields = '__all__'