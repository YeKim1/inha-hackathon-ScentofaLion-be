from django.shortcuts import render
from pyparsing import str_type
from .models import subSet
from .serializers import subSetSerializer
from account.models import User
from product.models import product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
import datetime

class subSet_API(APIView):
    def post(self, request, userId):
        set = subSet()
        user = User.objects.get(id=userId)
        set.diffuser = request.data["diffuser"]
        set.handwash = request.data["handwash"]
        set.handcream = request.data["handcream"]
        set.softner = request.data["softner"]
        set.perfume = request.data["perfume"]
        set.shampoo = request.data["shampoo"]
        set.rinse = request.data["rinse"]
        set.bodywash = request.data["bodywash"]
        set.candle = request.data["candle"]
        set.room = request.data["room"]
        set.bodymist = request.data["bodymist"]
        set.bodylotion = request.data["bodylotion"]        
        set.price = request.data["price"]
        set.date = datetime.date.today()
        set.save()
        
        user.subSet = set
        user.price = request.data["price"]
        user.sub_date = datetime.date.today()
        user.save()
        return Response(status=200)

    def get(self, request, userId):
        user = User.objects.get(id=userId)
        user_set = user.subSet
        set = subSet.objects.get(id=user_set.id)
        serializer = subSetSerializer(set)

        return Response(serializer.data, status=200)