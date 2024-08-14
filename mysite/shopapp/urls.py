from .views import shop_index, products_list
from django.urls import path

app_name = "shopapp"
urlpatterns = [
    path("", shop_index, name="index"),
    path("products/", products_list, name="products_list")
]