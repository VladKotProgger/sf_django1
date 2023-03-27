from django.views.generic import ListView, DetailView
from .models import Product


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    # queryset = Product.objects.order_by(
    #     '-name'
    # )
    template_name = 'products.html'
    context_object_name = 'products'


class ProductDetail(DetailView):
    model = Product
    ordering = '-name'
    template_name = 'product.html'
    context_object_name = 'product'
