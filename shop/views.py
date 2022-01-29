from django.shortcuts import render
from django.http import HttpResponse
from paytmchecksum import PaytmChecksum
import requests
import json
from .models import product, contact, Order, UpdateOrder
from math import ceil
import json
import datetime
from django.views.decorators.csrf import csrf_exempt
from paytm import Checksum
MERCHANT_KEY = "6PiKpXfE&sBHw3rN"
MERCHANT_ID = "AVjbPn81825059245113"
import paytmchecksum


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
def searchMatch(query, item):

       if query in item.desc.lower() or query in item.product_name.lower() or query in item.category:
           return True
       else:
           return False




def search(request):
    query = request.GET.get("search")
    all_prod = []
    catpods = product.objects.values("category", "id")
    cats = {item["category"] for item in catpods}

    for cat in cats:
        prodstemp = product.objects.filter(category=cat)
        prods = [item for item in prodstemp if searchMatch(query, item)]

        n = len(prods)
        nSlides = (n // 4) + ceil((n / 4) - (n // 4))
        if (len(prods)!=0):
             all_prod.append([prods, range(1, nSlides), nSlides])

    param = {"all_products": all_prod, "msg": ""}
    if len(all_prod) == 0 or len(query) < 4:
        param = {"msg": "Pleasea make a relevant search"}
    return render(request, "shop/search.html", param)










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
                 paytmParams = dict()

                 paytmParams["body"] = {
                     "requestType"   :   "Payment",
                     "mid"           :    MERCHANT_ID,
                     "websiteName"  :  "WEBSTAGING",
                     "orderId"        :   str(order.order_id),
                     "callbackUrl"    :  "http://127.0.0.1:8000/shop/handlerequest/",
                     "txnAmount"    :   {
                                  "value": str(amount),
                                  "currency": "INR",
                     },
                     "userInfo"        : {
                          "custId": "CUST_001",
                     },
                 }
                 checksum = PaytmChecksum.generateSignature(json.dumps(paytmParams["body"]), MERCHANT_KEY)
                 paytmParams["head"] = {
                     "signature": checksum
                 }
                 post_data = json.dumps(paytmParams)
                 url = f"https://securegw-stage.paytm.in/theia/api/v1/initiateTransaction?mid=AVjbPn81825059245113&orderId={str(order.order_id)}"
                 response = requests.post(url, data=post_data, headers={"Content-type": "application/json"}).json()
                 print(response)
                 form_data = {
                      "mid": MERCHANT_ID,
                     "txnToken": response["body"]["txnToken"],
                     "order_id": paytmParams["body"]["orderId"]
                 }

                 return render(request, 'shop/CheckoutJS.html', {"data": form_data})
        return render(request, 'shop/checkout.html')

def products(request, my_id):

        products = product.objects.filter(id = my_id)

        return render(request, "shop/productview.html", {"product": products[0]})



def thank(request,id):

    return render(request, "shop/thank.html",{"id": id})



@csrf_exempt
def handlerequest(request):


    # Create a Dictionary from the parameters received in POST
    # received_data should contains all data received in POST
        paytmParam= {}

        received_data = request.POST
        print(received_data)
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                   paytmChecksum = value
            else:
                    paytmParam[key] = value

    # Verify checksum
    # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
        isValidChecksum = Checksum.verify_checksum(paytmParam, MERCHANT_KEY, paytmChecksum)
        if isValidChecksum:
             print("Checksum Matched")
        else:
              print("Checksum Mismatched")

        return render(request, 'shop/paymentstatus.html', {'response': paytmParam})



