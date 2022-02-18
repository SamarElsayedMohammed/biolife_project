from django.contrib.auth.mixins import (
LoginRequiredMixin,
PermissionRequiredMixin 
)

from django.views.generic import ListView ,DetailView
from .models import Product

class ShopListView(LoginRequiredMixin,ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/shop.html'
    login_url = 'account_login'

class ProductDetailView(LoginRequiredMixin ,PermissionRequiredMixin,DetailView): 
    model = Product
    context_object_name ="product"
    template_name = 'products/product_details.html'
    login_url = 'account_login'
    permission_required = 'products.special_status'
