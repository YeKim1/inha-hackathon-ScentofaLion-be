from django.contrib import admin
from django.urls import path
from account import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('login/', csrf_exempt(views.login.as_view()), name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', csrf_exempt(views.signup.as_view()), name="signup"),
]
