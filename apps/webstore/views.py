from django.shortcuts import render
from .models import *
# Create your views here.

def kayu(request):
    return render(request, 'index.html')
def shop(request):
    allproductos=productos.objects.all()
    return render(request, 'prodact-display.html',{'allproductos':allproductos})

def blog(request):
    return render(request, 'single-product.html')