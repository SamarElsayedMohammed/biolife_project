from django.urls import path

from .views import ShopListView ,ProductDetailView
urlpatterns = [
    path('', ShopListView.as_view(), name='shop_list'),
    path('<uuid:pk>', ProductDetailView.as_view(), name='product_details'),
]
