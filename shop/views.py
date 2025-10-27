from django.shortcuts import render

from shop.models import Product


# Later I'll add logic for post request where click on btn add product to cart
def shop_view(request):
    products = Product.objects.all()
    return render(request, 'shop/shop-page.html', {'products': products})
