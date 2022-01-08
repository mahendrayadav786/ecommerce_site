from django.shortcuts import render
from django.http import HttpResponse
from .models import product, contact
from math import ceil

def index(request):


        all_prod=[]
        catpods = product.objects.values("category", "id")
        cats = {item["category"] for item in catpods}
        print(cats)
        for cat in cats:
                prods = product.objects.filter(category=cat)
                n = len(prods)
                nSlides = (n // 4) + ceil((n / 4) - (n // 4))

                all_prod.append([prods, range(1, nSlides), nSlides])
        param = {"all_products": all_prod}
        return render(request, "shop/index.html", param)


def about(request):

        return render(request, "shop/about.html")

def contactus(request):
        if request.method == "POST":
                user_name = request.POST.get("user_name", "")
                email = request.POST.get("email", "")
                phone = request.POST.get("phone", "")
                desc = request.POST.get("desc", "")
                contactus =contact(name=user_name, phone = phone, desc = desc, email = email)
                contactus.save()
        return render(request, "shop/contactus.html")

def tracker(request):
        return render(request, "shop/tracker.html")

def checkout(request):

        return render(request, "shop/checkout.html")

def products(request, my_id):

        products = product.objects.filter(id = my_id)
        print(products)
        return render(request, "shop/productview.html", {"product": products[0]})

def search(request):

    return HttpResponse("search us page")




