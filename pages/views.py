from django.shortcuts import render

from products.models import Products
def index(request):
    categories = Products.objects.all()
    men_products = Products.objects.filter(status=Products.Status.Published).filter(category__name="Men")[:]
    women = Products.objects.filter(status=Products.Status.Published).filter(category__name="Women")[:]
    kids_products = Products.objects.filter(status=Products.Status.Published).filter(category__name="Kids")[:]
    watches = Products.objects.filter(status=Products.Status.Published).filter(category__name="Watches")[:]
    shoes = Products.objects.filter(status=Products.Status.Published).filter(category__name="Shoes")[:]

    context = {
        'categories': categories,
        'men': men_products,
        'women': women,
        'kids': kids_products,
        'watches': watches,
        'shoes': shoes

    }

    return render(request, 'shop/index.html', context)


def about(request):
    return render(request, 'shop/about.html')

def blog(request):
    return render(request, 'shop/blog.html')

def blog_detail(request):
    return render(request, 'shop/blog-detail.html')

def contact(request):
    return render(request, 'shop/contact.html')

def home2(request):
    return render(request, 'shop/home-02.html')

def home3(request):
    categories = Products.objects.all()
    men_products = Products.objects.filter(status=Products.Status.Published).filter(category__name="Men")[:]
    women = Products.objects.filter(status=Products.Status.Published).filter(category__name="Women")[:]
    kids_products = Products.objects.filter(status=Products.Status.Published).filter(category__name="Kids")[:]
    watches = Products.objects.filter(status=Products.Status.Published).filter(category__name="Watches")[:]
    shoes = Products.objects.filter(status=Products.Status.Published).filter(category__name="Shoes")[:]

    context = {
        'categories': categories,
        'men': men_products,
        'women': women,
        'kids': kids_products,
        'watches': watches,
        'shoes': shoes

    }

    return render(request, 'shop/home-03.html', context)

def product(request):

        categories = Products.objects.all()
        men_products = Products.objects.filter(status=Products.Status.Published).filter(category__name="Men")[:]
        women = Products.objects.filter(status=Products.Status.Published).filter(category__name="Women")[:]
        kids_products = Products.objects.filter(status=Products.Status.Published).filter(category__name="Kids")[:]
        watches = Products.objects.filter(status=Products.Status.Published).filter(category__name="Watches")[:]
        shoes = Products.objects.filter(status=Products.Status.Published).filter(category__name="Shoes")[:]

        context = {
            'categories': categories,
            'men': men_products,
            'women': women,
            'kids': kids_products,
            'watches': watches,
            'shoes': shoes

        }

        return render(request, 'shop/product.html', context)

def product_detail(request):
    return render(request, 'shop/product-detail.html')

def shopping_cart(request):
    return render(request, 'shop/shoping-cart.html')