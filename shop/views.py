from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
        return render(request, "shop/index.html")

def about(request):
        return HttpResponse("about us page")
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




