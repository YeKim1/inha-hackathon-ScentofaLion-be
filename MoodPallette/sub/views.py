from django.shortcuts import render
from pyparsing import str_type
from .models import subSet
from .serializers import subSetSerializer, NameSerializer, TFSerializer
from account.models import User
from product.models import product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

class subSet_API(APIView):
    def post(self, request, userId):
        set = subSet()
        user = User.objects.get(id=userId)
        for k, v in request.data.items():
            p = product.objects.get(pk=v)
            if k == "diffuser":
                set.diffuser = p
                set.count += 1
            elif k == "handwash":
                set.handwash = p
                set.count += 1
            elif k == "handcream":
                set.handcream = p
                set.count += 1
            elif k == "sofrner":
                set.sofrner = p
                set.count += 1
            elif k == "perfume":
                set.perfume = p
                set.count += 1
            elif k == "shampoo":
                set.shampoo = p
                set.count += 1
            elif k == "rinse":
                set.rinse = p
                set.count += 1
            elif k == "bodywash":
                set.bodywash = p
                set.count += 1
            elif k == "candle":
                set.candle = p
                set.count += 1
            elif k == "room":
                set.room = p
                set.count += 1
            elif k == "bodymist":
                set.bodymist = p
                set.count += 1
            elif k == "bodylotion":
                set.bodylotion = p
                set.count += 1
                
        set.color = user.user_color
        set.save()
        user.subSet = set
        user.save()
        return Response(status=200)

    def get(self, request, userId):
        user = User.objects.get(id=userId)
        user_set = user.subSet
        set = subSet.objects.get(id=user_set.id)
        serializer = subSetSerializer(set)

        return Response(serializer.data, status=200)

class sub_product(APIView):
    def get(self, request, userId):
        user = User.objects.get(id=userId)
        user_set = user.subSet
        set = subSet.objects.get(id=user_set.id)

        serializer = NameSerializer(set)
        
        list = {}

        for k,v in serializer.data.items():
            if v:
                list[k] = v

        return Response(list, status=200)
