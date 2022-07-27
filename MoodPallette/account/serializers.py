from importlib.metadata import files
from rest_framework import serializers
from .models import User

class accountSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'price', 'sub_date', 'nickname', 'subSet', 'user_color')
        