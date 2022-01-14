from django.shortcuts import render
from django.http import HttpResponse
from .models import product, contact, Order
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
        if request.method == "POST":
                 item_json = request.POST.get("item_json", "")
                 name = request.POST.get("name", "")
                 email = request.POST.get("email", "")
                 phone = request.POST.get("phone", "")
                 city = request.POST.get("city", "")
                 state = request.POST.get("state", "")
                 zip_code = request.POST.get("zip_code", "")
                 address = request.POST.get("address1", "") + " " + request.POST.get("address2", "")




                 order = Order(item_json= item_json, name=name, phone=phone, city=city, email=email, state = state, zip_code = zip_code, address= address)
                 order.save()
                 id = order.order_id
                 thank = True

                 return render(request, "shop/checkout.html", {"thank":thank, "id": id})



        return render(request, "shop/checkout.html")

def products(request, my_id):

        products = product.objects.filter(id = my_id)
        print(products)
        return render(request, "shop/productview.html", {"product": products[0]})

def search(request):

    return HttpResponse("search us page")

def thank(request,id):

    return render(request, "shop/thank.html",{"id": id})



