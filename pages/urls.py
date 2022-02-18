# pages/urls.py
from django.urls import path
from .views import HomePageView,ShopPageView,ProductsPageView,BlogPageView,ContactPageView,AboutUsPageView,CheckOutPageView,LoginPageView,SignUpPageView,ErrorPageView,FavoratePageView,ProductDetailsPageView,BlogDetailsPageView,CartPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('shop/',ShopPageView.as_view(),name='shop'),
    # path('products/',ProductsPageView.as_view(),name='productss'),
    path('blog/',BlogPageView.as_view(),name='blog'),
    path('contact/',ContactPageView.as_view(),name='contact'),
    path('about-us/',AboutUsPageView.as_view(),name='about-us'),
    path('check-out/',CheckOutPageView.as_view(),name='check-out'),
    # path('login/',LoginPageView.as_view(),name='login'),
    path('sign_up/',SignUpPageView.as_view(),name='sign_up'),
    path('404/',ErrorPageView.as_view(),name='404'),
    path('favorate/',FavoratePageView.as_view(),name='favorate'),
    path('product_details/',ProductDetailsPageView.as_view(),name='product_details'),
    path('blog_details/',BlogDetailsPageView.as_view(),name='blog_details'),
    path('cart/',CartPageView.as_view(),name='cart'),
]