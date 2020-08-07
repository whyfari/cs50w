
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

import datetime

# Create your views here.


def index(request):
    now = datetime.datetime.now()
    print("blai", now)

    return render(request, "newyear/index.html")
    # return render(request, "newyear/index.html", {
    #     "newYear": now.year == 1 and now.month == 1
    # })
