from django.db.models import Q
from django.shortcuts import render,  get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Products


def products_detail(request, slug):
    product = get_object_or_404(Products, slug=slug)
    return render(request, 'shop/product-detail.html', {'product': product})


#pastdagi kod hamePageView uchun sababi bu kod funksiyani ichida iwlamadi
x = Products.objects.filter(status=Products.Status.Published)

class MenPageView(ListView):
    model = Products
    template_name = 'shop/men.html'
    context_object_name = 'mens'

    def get_queryset(self):
        products = Products.objects.filter(status=Products.Status.Published).filter(category__name="Men")
        return products

class WomanView(ListView):
    model = Products
    template_name = 'shop/women.html'
    context_object_name = 'women'

    def get_queryset(self):
        products = Products.objects.filter(status=Products.Status.Published).filter(category__name="Women")
        return products

class KidsView(ListView):
    model = Products
    template_name = 'shop/kids.html'
    context_object_name = 'kids'

    def get_queryset(self):
        news = Products.objects.filter(status=Products.Status.Published).filter(category__name="Kids")
        return news

class WatchesPageView(ListView):
    model = Products
    template_name = 'shop/watches.html'
    context_object_name = 'watches'

    def get_queryset(self):
        news = Products.objects.filter(status=Products.Status.Published).filter(category__name="Watches")
        return news


class ProductsUpdateView(UpdateView):
    model = Products
    fields = ('title', 'price', 'image', 'category', 'status', )
    template_name = "crud/products_edit.html"

class ProductsDeleteView(DeleteView):
    model = Products
    template_name = "crud/products_delete.html"
    success_url = reverse_lazy('home_page')

class ProductsCreateView(CreateView):
    model = Products
    template_name = "crud/products_create.html"
    fields = ('title', 'slug', 'price', 'image', 'category', 'status')

class SearchResultList(ListView):
    model = Products
    template_name = 'shop/search_result.html'
    context_object_name = 'search'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Products.objects.filter(
            Q(title__icontains=query) | Q(price__icontains=query) | Q(body__icontains=query)
        )


