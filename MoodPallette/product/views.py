from django.shortcuts import render,redirect
from .models import product
from .serializers import ProductSerializer
from account.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

# Create your views here.

class red(APIView):
    def get(self, request, *args, **kwargs):
        red_product = product.objects.filter(product_color="RED")
        serializer = ProductSerializer(red_product, many=True)
        return Response(serializer.data, status=200)

class yellow(APIView):
    def get(self, request, *args, **kwargs):
        yellow_product = product.objects.filter(product_color="YELLOW")
        serializer = ProductSerializer(yellow_product, many=True)
        return Response(serializer.data, status=200)

class green(APIView):
    def get(self, request, *args, **kwargs):
        green_product = product.objects.filter(product_color="GREEN")
        serializer = ProductSerializer(green_product, many=True)
        return Response(serializer.data, status=200)

class blue(APIView):
    def get(self, request, *args, **kwargs):
        blue_product = product.objects.filter(product_color="BLUE")
        serializer = ProductSerializer(blue_product, many=True)
        return Response(serializer.data, status=200)

class black(APIView):
    def get(self, request, *args, **kwargs):
        black_product = product.objects.filter(product_color="BLACK")
        serializer = ProductSerializer(black_product, many=True)
        return Response(serializer.data, status=200)

class white(APIView):
    def get(self, request, *args, **kwargs):
        white_product = product.objects.filter(product_color="WHITE")
        serializer = ProductSerializer(white_product, many=True)
        return Response(serializer.data, status=200)

class purple(APIView):
    def get(self, request, *args, **kwargs):
        purple_product = product.objects.filter(product_color="PURPLE")
        serializer = ProductSerializer(purple_product, many=True)
        return Response(serializer.data, status=200)

class getuser(APIView):
    def get(self, request, userId):
        user = User.objects.get(id=userId)
        print(user.sbti)
        user_product = product.objects.filter(product_color=user.sbti)
        serializer = ProductSerializer(user_product, many=True)
        return Response(serializer.data, status=200)
