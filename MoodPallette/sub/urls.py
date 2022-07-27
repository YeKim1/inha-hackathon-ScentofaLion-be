from django.contrib import admin
from django.urls import path
from sub import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('<int:userId>/', csrf_exempt(views.subSet_API.as_view())),
    path('<int:userId>/count/', csrf_exempt(views.subSet_TF.as_view())),
]
