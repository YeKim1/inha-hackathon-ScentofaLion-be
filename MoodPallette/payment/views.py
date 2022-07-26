from django.shortcuts import render, get_object_or_404
from .models import payment
from .serializers import PaymentSerializer, PaymentPutSerializer
from account.models import User
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class getpay(APIView):
    def post(self, request, userId):
        user = User.objects.get(id=userId)
        pay = payment()
        pay.email = user.email
        pay.pay_price = request.data['pay_price']
        pay.pay_date = request.data['pay_date']
        pay.pay_method = request.data['pay_method']
        pay.save()
        return Response(status=200)

    def get(self, request, userId):
        user = User.objects.get(id=userId)
        pay = payment.objects.filter(email=user.email).order_by("-pay_date")
        serializer = PaymentSerializer(pay, many=True)
        return Response(serializer.data, status=200)

    # def put(self, request, userId, format=None):
    #     user = get_object_or_404(User, id=userId)
    #     serializer = PaymentPutSerializer(user, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=400)

    