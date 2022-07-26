from django.shortcuts import render
from .models import subSet
from .serializers import subSetSerializer, NameSerializer
from account.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

class subSet_API(APIView):
    def post(self, request, userId):
        set = subSet()
        user = User.objects.get(id=userId)
        set.subSelect_id = user.subSelect_id
        set.diffuser_name = request.data['diffuser_name']
        set.handwash_name = request.data['handwash_name']
        set.handcream_name = request.data['handcream_name']
        set.sofrner_name = request.data['sofrner_name']
        set.perfume_name = request.data['perfume_name']
        set.shampoo_name = request.data['shampoo_name']
        set.rinse_name = request.data['rinse_name']
        set.bodywash_name = request.data['bodywash_name']
        set.candle_name = request.data['candle_name']
        set.room_name = request.data['room_name']
        set.bodymist_name = request.data['bodymist_name']
        set.bodylotion_name = request.data['bodylotion_name']
        set.save()
        
        return Response(set.data)

    def get(self, request, userId):
        user = User.objects.get(id=userId)
        set = subSet.objects.get(subSelect_id = user.subSelect_id)
        serializer = subSetSerializer(set, many=True)
        return Response(serializer, status=200)

    def put(self, request, userId):
        user = User.objects.get(id=userId)
        set = subSet.objects.get(subSelect_id = user.subSelect_id)
        serializer = NameSerializer(set, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
