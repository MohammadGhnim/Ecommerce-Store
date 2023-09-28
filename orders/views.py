from django.shortcuts import render
from django.views.generic import ListView
from .models import Order

# Create your views here.


class OrderList(ListView):
    model = Order