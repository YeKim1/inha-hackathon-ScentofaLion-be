from rest_framework import serializers
from .models import subSet

class subSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = subSet
        fields = '__all__'

class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = subSet
        exclude = ['id', 'color']

class TFSerializer(serializers.ModelSerializer):
    class Meta:
        model = subSet
        fields = ['count']
