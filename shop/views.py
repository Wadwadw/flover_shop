from django.shortcuts import render
from django.views import generic
from .models import Product


def hello(request):
    return render(request, 'base.html')


class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products_list.html'






