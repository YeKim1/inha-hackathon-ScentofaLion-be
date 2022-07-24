from django.contrib import admin
from django.urls import path
from product import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name="create"),

]
