from django.urls import path
from .views import add_product, get_product_details, get_all_products

urlpatterns = [
    path('add-product/', add_product, name='add_product'),
    path('product/<str:barcode>/', get_product_details, name='get_product_details'),
    path('all-products/', get_all_products, name='get_all_products'),
]
