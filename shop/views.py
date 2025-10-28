from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse

import json

from shop.models import Product
from orders.models import Order, OrderItem


def shop_view(request: HttpRequest):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        order_items = data.get('items', [])
        total = data.get('total', 0)
        print(order_items, total)
        return JsonResponse({'redirect_url': 'home'})
    products = Product.objects.all()
    return render(request, 'shop/shop-page.html', {'products': products})


def create_cart_view(request: HttpRequest):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        return HttpResponse('DONE')
