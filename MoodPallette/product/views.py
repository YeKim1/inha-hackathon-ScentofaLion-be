from django.shortcuts import render,redirect
from .models import product

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


def home(request):
    products = product.objects.all()
    return render(request, 'home.html', {'products':products})



