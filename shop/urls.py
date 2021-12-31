from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name = "ShopHome"),
    path("about/", views.about, name = "Aboutus"),
    path("contactus/", views.contactus, name = "contactus"),
    path("tracker/", views.tracker, name = "tracker"),
    path("productview/", views.productview, name = "productview"),
    path("search/", views.search, name = "search"),
    path("checkout/", views.checkout, name = "checkout"),


]
