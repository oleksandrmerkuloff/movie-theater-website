from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, JsonResponse
from django.urls import reverse

import json
from typing import Any

from shop.models import Product
from orders.models import Order, OrderItem


def shop_view(request: HttpRequest):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({'redirect_url': reverse('login')})
        data = json.loads(request.body.decode('utf-8'))
        order_items = data.get('items', [])
        total = data.get('total', 0)
        new_order = Order.objects.create(
            user=request.user,
            total_text=total,
            status='np'
        )
        for item in order_items.values():
            OrderItem.objects.create(
                name=item['name'],
                price_text=item['price'],
                quantity=item['qty'],
                order=new_order
            )
        return JsonResponse({
            'redirect_url': reverse('confirm', args=[new_order.pk])
        })
    products = Product.objects.all()
    return render(request, 'shop/shop-page.html', {'products': products})


def confirmation_view(request: HttpRequest, order_id: Any):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'shop/confirmation.html', {'order': order})
