from django.shortcuts import render
from .models import ProductCategory, Product

def main(request):
    products = Product.objects.all()[:4]
    links_menu = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'products:index', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'},
    ]

    content = {
        'title': 'Магазин',
        'links': links_menu,
        'products': products
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request, pk=None):
    product_category = ProductCategory.objects.all()
    links_menu = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'products:index', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'},
    ]

    content = {
        'title': 'Каталог',
        'links': links_menu,
        'product_category': product_category
    }
    return render(request, 'mainapp/products.html', context=content)


def contact(request):
    links_menu = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'products:index', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'},
    ]

    content = {
        'title': 'Контакты',
        'links': links_menu
    }
    return render(request, 'mainapp/contact.html', context=content)
