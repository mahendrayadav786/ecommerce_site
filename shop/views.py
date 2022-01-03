from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from math import ceil
# Create your views here.
def index(request):
        products = product.objects.all()
        print(products)
        n = len(products)
        nSlides = (n//4)+ceil((n/4) - (n//4))
        param = {"nslides": nSlides, "range": range(1, nSlides), "product": products}
        return render(request, "shop/index.html", param)

def about(request):
        return render(request, "shop/about.html")
def contactus(request):
        return HttpResponse("contact us page")

def tracker(request):
        return HttpResponse("tracker us page")

def checkout(request):
        return HttpResponse("checkout us page")

def productview(request):
        return HttpResponse("productview us page")
def search(request):
    return HttpResponse("search us page")




