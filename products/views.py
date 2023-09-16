from typing import Any
from django.db.models.query import QuerySet
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

class BrandDetail(generic.ListView):
    model=Product
    template_name='product/brand_detail.html'

    def get_queryset(self):
        brand=Brand.objects.get(slug=self.kwargs['slug'])
        queryset=Product.objects.filter(brand=brand)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.get(slug=self.kwargs['slug'])
        return context
    