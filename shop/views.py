from django.shortcuts import render
from django.views import generic
from .models import Product, Ip


def get_user_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


class ProductListView(generic.ListView):
    model = Product
    context_object_name = "products"
    template_name = "products_list.html"


def product_detail(request, slug: str):
    product = Product.objects.get(slug=slug)

    ip = get_user_ip(request)
    print(ip)
    if Ip.objects.filter(ip=ip).exists():
        product.views.add(Ip.objects.get(ip=ip))
    else:
        Ip.objects.create(ip=ip)
        product.views.add(Ip.objects.get(ip=ip))

    context = {"product": product}
    return render(request, "product_detail.html", context=context)
