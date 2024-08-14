from django.shortcuts import render
from timeit import default_timer
from django.http import HttpRequest
from .models import Product, Order


def shop_index(request: HttpRequest):
    products = [
        ("холодИльник ", 11000),
        ("пЛита", 20000),
        ("тостеР", 2000),
    ]

    context = {
        "time_running": default_timer(),
        "products": products,
    }
    return render(request, "shopapp/shop-index.html", context=context)


def orders_list(request: HttpRequest):
    context = {
        "orders": Order.objects.select_related("user").all(),
    }
    return render(request, 'shopapp/orders-list.html', context=context)


def products_list(request: HttpRequest):
    context = {
        "products": Product.objects.all(),
    }
    return render(request, 'shopapp/products-list.html', context=context)
