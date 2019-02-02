from django.shortcuts import render, redirect

from django.views.generic import ListView, DeleteView, CreateView, View
from .models import Comporisoon

from mainApp.models import Product
# from .forms import ComporisoonForm
# deleteView
from django.urls import reverse_lazy

## Create your views here.

# class AddComporisoon(View):
#     def post(self, request, id):
#         product = Product.objects.filter(pk=id)
#         form = ComporisoonForm(request.Post)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.productId = product
#             instance.save()
#


class ComporisoonProduct(ListView):
    context_object_name = 'comporisoonProduct'
    model = Comporisoon
    def get_queryset(self, *args, **kwargs):
        sq = super(ComporisoonProduct, self).get_queryset(*args, **kwargs).exclude()[:4]
        return sq

# class DeleteComporisoon(DeleteView):
#     context_object_name = 'deleteComporisoon'
#     template_name = 'productActivite/comporisoon_list.html'
#     model = Comporisoon
#     success_url =  reverse_lazy('productA:delete')

def delete_comporision(self, id):
    item = Comporisoon.objects.filter(pk=id)
    item.delete()
    return redirect('comporisoonActivite:comporisoon')