from django.shortcuts import render
from django.views import generic
from .models import Product, ProductImages, Review, Brand

# Create your views here.

class ProductList(generic.ListView):
    model=Product

class ProductDetail(generic.DeleteView):
    model=Product