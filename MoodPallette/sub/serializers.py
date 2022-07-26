from rest_framework import serializers
from .models import subSet, subSelect

class subSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = subSet
        fields = ('color', 'diffuser_name', 'handwash_name', 'handcream_name', 'sofrner_name', 'perfume_name', 'shampoo_name', 'rinse_name', 'bodywash_name', 'candle_name', 'room_name', 'bodymist_name', 'bodylotion_name')

class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = subSet
        fields = ('diffuser_name', 'handwash_name', 'handcream_name', 'sofrner_name', 'perfume_name', 'shampoo_name', 'rinse_name', 'bodywash_name', 'candle_name', 'room_name', 'bodymist_name', 'bodylotion_name')

class subSelectSerializer(serializers.ModelField):
    class Meta:
        model = subSelect
        fields = '__all__'