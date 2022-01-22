from django.shortcuts import render
from django.http import HttpResponse
from . models import Blogpost
# Create your views here.
def index(request):

    posts = Blogpost.objects.all()
    all_post = []
    for post in posts:
        all_post.append(post)

    return render(request, "blog/index.html", {"all_post": all_post})


def blogpost(request):
    return render(request, "blog/blogpost.html")