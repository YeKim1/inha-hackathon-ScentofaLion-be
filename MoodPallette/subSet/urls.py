from django.contrib import admin
from django.urls import path
from subSet import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('<int:userId>/create/', csrf_exempt(views.subSet_API.as_view())),
    path('<int:userId>/', csrf_exempt(views.subSet_API.as_view())),
    path('<int:userId>/update', csrf_exempt(views.subSet_API.as_view())),
]

