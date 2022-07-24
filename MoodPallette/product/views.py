from django.shortcuts import render,redirect
from .models import product
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

# Create your views here.

def create(request):
    if(request.method=="POST"):
        pd = product()
        pd.product_name = request.POST['product_name']
        pd.product_color = request.POST['product_color']
        pd.product_type = request.POST['product_type']
        pd.product_img = request.POST['product_img']
        pd.save()
        return redirect('create')
    else:
        return render(request, 'create.html')

class red(APIView):
    def get(self, request, *args, **kwargs):
        red_product = product.objects.filter(product_color="red")
        serializer = ProductSerializer(red_product, many=True)
        return Response(serializer.data, status=200)

class yellow(APIView):
    def get(self, request, *args, **kwargs):
        yellow_product = product.objects.filter(product_color="yellow")
        serializer = ProductSerializer(yellow_product, many=True)
        return Response(serializer.data, status=200)

class green(APIView):
    def get(self, request, *args, **kwargs):
        green_product = product.objects.filter(product_color="green")
        serializer = ProductSerializer(green_product, many=True)
        return Response(serializer.data, status=200)

class blue(APIView):
    def get(self, request, *args, **kwargs):
        blue_product = product.objects.filter(product_color="blue")
        serializer = ProductSerializer(blue_product, many=True)
        return Response(serializer.data, status=200)

class black(APIView):
    def get(self, request, *args, **kwargs):
        black_product = product.objects.filter(product_color="black")
        serializer = ProductSerializer(black_product, many=True)
        return Response(serializer.data, status=200)

class white(APIView):
    def get(self, request, *args, **kwargs):
        white_product = product.objects.filter(product_color="white")
        serializer = ProductSerializer(white_product, many=True)
        return Response(serializer.data, status=200)

class purple(APIView):
    def get(self, request, *args, **kwargs):
        purple_product = product.objects.filter(product_color="purple")
        serializer = ProductSerializer(purple_product, many=True)
        return Response(serializer.data, status=200)