from rest_framework import serializers
from .models import payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment
        fields = ('id','email','pay_price','pay_date','pay_method')

class PaymentPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment
        fields = ('pay_price','pay_date','pay_method')