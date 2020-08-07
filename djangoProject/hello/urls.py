from django.urls import path

from . import views


urlpatterns = [
    # first art is route, empty for this case
    # second arg view - index views(views.py file, we imported it above).index(function in that file)
    # remaining args are 'kargs' so you specify the name of argument and value, like 'name' with value 'index' (this is optional)
    path("", views.index, name="index"),
    path("fari", views.fari, name="fari"),
    path("<str:name>", views.greet, name="greet"),
]
