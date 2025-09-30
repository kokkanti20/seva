from django.urls import path
from . import views

urlpatterns = [
    path("", views.sos_home, name="sos_home"),
    path("send/", views.sos_send, name="sos_send"),
]
