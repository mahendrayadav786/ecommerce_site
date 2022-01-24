from django.shortcuts import render
from django.http import HttpResponse
from .models import product, contact, Order, UpdateOrder
from math import ceil
import json
import datetime
from django.views.decorators.csrf import csrf_exempt
from paytm import Checksum
MERCHANT_KEY = "kbzk1DSbJiV-03p5"
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
        thank = False
        if request.method == "POST":
                user_name = request.POST.get("user_name", "")
                email = request.POST.get("email", "")
                phone = request.POST.get("phone",)
                desc = request.POST.get("desc", "")
                contactus =contact(name=user_name, phone = phone, desc = desc, email = email)
                contactus.save()
                thank = True

        return render(request, "shop/contactus.html", {"thank": thank})

def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', "")
        email = request.POST.get('email', "")
        try:
            order =Order.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update =UpdateOrder.objects.filter(order_id=orderId)
                updates = []
                for item in update:

                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)

                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
             return HttpResponse('{}')

        return render(request, 'shop/tracker.html')

    return render(request, "shop/tracker.html")

def checkout(request):

        if request.method == "POST":
                 item_json = request.POST.get("item_json", "")
                 amount = request.POST.get("amount", "")

                 name = request.POST.get("name", "")
                 email = request.POST.get("email", "")
                 phone = request.POST.get("phone", "")
                 city = request.POST.get("city", "")
                 state = request.POST.get("state", "")
                 zip_code = request.POST.get("zip_code", "")
                 address = request.POST.get("address1", "") + " " + request.POST.get("address2", "")

                 order = Order(item_json= item_json, name=name, phone=phone, city=city, email=email, state = state, zip_code = zip_code, address= address, amount = amount)
                 order.save()
                 x =datetime.datetime.now()
                 order = UpdateOrder(order_id = order.order_id, update_desc = "You order has been placed", timestamp= x.strftime("%b"+" "+"%d"+", "+"%Y"+" "+"%H"+":"+"%M"))
                 order.save()
                 id = order.order_id
                 thank = True

                 # return render(request, "shop/checkout.html", {"thank":thank, "id": id})
              ##request paytm to tak emoney from the user and send it to your account
                 param_dict = {

                     'MID': 'WorldP64425807474247',
                     'ORDER_ID': str(order.order_id),
                     'TXN_AMOUNT': str(amount),
                     'CUST_ID': email,
                     'INDUSTRY_TYPE_ID': 'Retail',
                     'WEBSITE': 'WEBSTAGING',
                     'CHANNEL_ID': 'WEB',
                     'CALLBACK_URL': 'http://127.0.0.1:8000/shop/handlerequest/',

                 }

                 param_dict["CHECKSUMHASH"] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
                 return render(request, "shop/paytm.html", {"param_dict": param_dict})
        return render(request, "shop/checkout.html")


def products(request, my_id):

        products = product.objects.filter(id = my_id)

        return render(request, "shop/productview.html", {"product": products[0]})

def search(request):

    return HttpResponse("search us page")

def thank(request,id):

    return render(request, "shop/thank.html",{"id": id})


@csrf_exempt
def handlerequest(request):
    ##Paytm will send a post request here
   pass







