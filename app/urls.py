from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("",views.home, name="home"),
    path("supplier", views.supplier,name="supplier"),
     path("clients", views.clients,name="clients"),
    path("contact", views.contact, name="contact")
]