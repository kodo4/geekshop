from django.shortcuts import render


def main(request):
    links_menu = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'products', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'},
    ]

    content = {
        'title': 'Магазин',
        'links': links_menu
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request):
    links_menu = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'products', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'},
    ]

    content = {
        'title': 'Каталог',
        'links': links_menu,
    }
    return render(request, 'mainapp/products.html', context=content)


def contact(request):
    links_menu = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'products', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'},
    ]

    content = {
        'title': 'Контакты',
        'links': links_menu
    }
    return render(request, 'mainapp/contact.html', context=content)
