from django.shortcuts import render

from .models import CartList
from django.views.generic import View, ListView
# Create your views here.

class CartView(ListView):
    context_object_name = 'cart'
    model = CartList
    def get_queryset(self, *args, **kwargs):
        qs = super(CartView, self).get_queryset(*args, *kwargs)
        return qs