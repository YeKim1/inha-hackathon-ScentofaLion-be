from django.shortcuts import render, get_object_or_404
from .models import payment
from .serializers import PaymentSerializer, PaymentPutSerializer
from account.models import User
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class getpay(APIView):
    def get(self, request, userId):
        user = User.objects.get(id=userId)
        print(user.price)
        user_price = payment.objects.filter(pay_price=user.price)
        serializer = PaymentSerializer(user_price, many=True)
        return Response(serializer.data, status=200)

    def put(self, request, userId, format=None):
        user = get_object_or_404(User, id=userId)
        serializer = PaymentPutSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    