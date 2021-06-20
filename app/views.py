from django.shortcuts import render
from . models import Products
# Create your views here.

def index(request):
    obj=Products.objects.all()
    return render(request,"index.html",{"obj":obj})

def productView(request,pk):
    obj=Products.objects.filter(id=pk)
    return render(request,"productview.html",{"obj":obj})