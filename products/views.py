from django.shortcuts import render
from django.views import generic
from .models import Product, ProductImages, Review, Brand

# Create your views here.

class ProductList(generic.ListView):
    model=Product

class ProductDetail(generic.DetailView):
    model=Product


class BrandList(generic.ListView):
    model=Brand

class BrandDetail(generic.DetailView):
    model=Brand