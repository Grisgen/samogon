from ensurepip import bootstrap
from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

class ProductsList(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'

class ProductsList_Bootstrap(ListView):
    model = Product
    template_name = 'products_bootstrap.html'
    context_object_name = 'products'
