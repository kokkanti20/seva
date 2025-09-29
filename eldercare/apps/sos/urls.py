from django.urls import path
from .views import trigger_sos

urlpatterns = [ path("", trigger_sos) ]
