# pages/views.py
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class ShopPageView(TemplateView):
    template_name ='shop.html'

class ProductsPageView(TemplateView):
    template_name ='products.html'

class BlogPageView(TemplateView):
    template_name ='blog.html'

class ContactPageView(TemplateView):
    template_name ='contact.html'

class AboutUsPageView(TemplateView):
    template_name ='about_us.html'

class CheckOutPageView(TemplateView):
    template_name ='check_out.html'

class LoginPageView(TemplateView):
    template_name ='login.html'

class SignUpPageView(TemplateView):
    template_name ='sign_up.html'

class ErrorPageView(TemplateView):
    template_name ='404.html'

class FavoratePageView(TemplateView):
    template_name ='favorite.html'

class ProductDetailsPageView(TemplateView):
    template_name ='product_details.html'

class BlogDetailsPageView(TemplateView):
    template_name ='blog_details.html'

class CartPageView(TemplateView):
    template_name ='cart.html'

