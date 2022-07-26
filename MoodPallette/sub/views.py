from django.shortcuts import render
from .models import subSet, subSelect
from .serializers import subSetSerializer, NameSerializer, subSelectSerializer
from account.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

class subSet_API(APIView):
    def post(self, request, userId):
        set = subSet()
        Select = subSelect()
        user = User.objects.get(id=userId)

        set.diffuser_name = request.data['diffuser_name']
        if request.data['diffuser_name'] != "":
            Select.diffuser_yn = True
        set.handwash_name = request.data['handwash_name']
        if request.data['handwash_name'] != "":
            Select.handwash_yn = True
        set.handcream_name = request.data['handcream_name']
        if request.data['handcream_name'] != "":
            Select.handcream_yn = True
        set.sofrner_name = request.data['sofrner_name']
        if request.data['sofrner_name'] != "":
            Select.sofrner_yn = True
        set.perfume_name = request.data['perfume_name']
        if request.data['perfume_name'] != "":
            Select.perfume_yn = True
        set.shampoo_name = request.data['shampoo_name']
        if request.data['shampoo_name'] != "":
            Select.shampoo_yn = True
        set.rinse_name = request.data['rinse_name']
        if request.data['rinse_name'] != "":
            Select.rinse_yn = True
        set.bodywash_name = request.data['bodywash_name']
        if request.data['bodywash_name'] != "":
            Select.bodywash_yn = True
        set.candle_name = request.data['candle_name']
        if request.data['candle_name'] != "":
            Select.candle_yn = True
        set.room_name = request.data['room_name']
        if request.data['room_name'] != "":
            Select.room_yn = True
        set.bodymist_name = request.data['bodymist_name']
        if request.data['bodymist_name'] != "":
            Select.bodymist_yn = True
        set.bodylotion_name = request.data['bodylotion_name']
        if request.data['bodylotion_name'] != "":
            Select.bodylotion_yn = True

        Select.save()

        user.subSelect_id = Select.id
        set.subSelect_id = Select.id
        set.color = user.user_color

        set.save()
        user.save()

        return Response(status=200)

    def get(self, request, userId):
        user = User.objects.get(id=userId)
        set = subSet.objects.get(subSelect_id = user.subSelect_id)
        serializer = subSetSerializer(set)

        return Response(serializer.data, status=200)

    def put(self, request, userId):
        user = User.objects.get(id=userId)
        set = subSet.objects.get(subSelect_id = user.subSelect_id)
        serializer = NameSerializer(set, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)

class subSelect_API(APIView):
    def get(self, request, userId):
        user = User.objects.get(id=userId)
        select = subSelect.objects.get(id = user.subSelect_id)
        serializer = subSelectSerializer(select, many=True)
        return Response(serializer, status=200)