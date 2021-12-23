from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product
from basketapp.models import Basket

LINKS_MENU = [
    {'href': 'main', 'name': 'домой'},
    {'href': 'products:index', 'name': 'продукты'},
    {'href': 'contact', 'name': 'контакты'},
]


def main(request):
    products = Product.objects.all()[:4]

    content = {
        'title': 'Магазин',
        'links_menu': LINKS_MENU,
        'products': products
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request, pk=None):
    print(pk)

    title = 'продукты'
    links_menu_category = ProductCategory.objects.all()

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': LINKS_MENU,
            'links_menu_category': links_menu_category,
            'category': category,
            'products': products,
            'basket': basket,
        }

        return render(request, 'mainapp/products_list.html', content)



    if pk:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}

    same_products = Product.objects.all()[3:5]

    content = {
        'title': title,
        'links_menu': LINKS_MENU,
        'links_menu_category': links_menu_category,
        'same_products': same_products
    }
    return render(request, 'mainapp/products.html', context=content)


def contact(request):
    content = {
        'title': 'Контакты',
        'links_menu': LINKS_MENU
    }
    return render(request, 'mainapp/contact.html', context=content)
