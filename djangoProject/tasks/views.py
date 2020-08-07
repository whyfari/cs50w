
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render


import datetime

# Create your views here.

tasks = ["foo", "bar", 'baz']


def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })


def add(request):
    return render(request, "tasks/add.html")
