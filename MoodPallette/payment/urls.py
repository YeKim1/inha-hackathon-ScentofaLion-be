from django.contrib import admin
from django.urls import path
from payment import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('<int:userId>/', csrf_exempt(views.getpay.as_view())),
]
