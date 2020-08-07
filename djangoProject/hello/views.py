from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, "hello/index.html")


def fari(request):
    return HttpResponse("Hellow, Fari!!")


def greet(request, name):
    return render(request, "hello/add.html", {
        "name": name.capitalize()
    })
