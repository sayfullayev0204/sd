from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('products/', product, name='products'),
    path('home2/', home2, name='home2'),
    path('home3/', home3, name='home3'),
    path('blog/', blog, name='blog'),
    path('cart/', shopping_cart, name='cart'),
    path('blog-detail/', blog_detail, name='blog_detail')
]