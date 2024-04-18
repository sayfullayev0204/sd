from django.urls import path

from .views import *

urlpatterns = [
    path('products/create/', ProductsCreateView.as_view(), name="news_create"),
    path('products/<slug>/product', products_detail, name="products_detail_page"),
    path('products/<slug>/edit/', ProductsUpdateView.as_view(), name="news_update"),
    path('products/<slug>/delete/', ProductsDeleteView.as_view(), name="news_delete"),
    path('mens/', MenPageView.as_view(), name="men"),
    path('women/', WomanView.as_view(), name="women"),
    path('kids/', KidsView.as_view(), name="kids"),
    path('watches/', WatchesPageView.as_view(), name="watches"),
    path('search-result/', SearchResultList.as_view(), name="search_results")
]