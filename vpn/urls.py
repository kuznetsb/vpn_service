from django.urls import path

from vpn.views import index

urlpatterns = [
    path("", index, name="index"),
]


app_name = "vpn"