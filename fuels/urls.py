from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Get_Price,name="price"),
    path('put_price', views.Put_Price,name="put_price"),
]