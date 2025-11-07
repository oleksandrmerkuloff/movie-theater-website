from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, JsonResponse
from django.urls import reverse
from django.contrib import messages

import json
from typing import Any

from shop.models import Product
from orders.models import Order, OrderItem
from shop.forms import PaymentForm


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

    if request.user.is_authenticated:
        Order.objects.filter(user=request.user).filter(status='np').delete()

    products = Product.objects.all()
    return render(request, 'shop/shop-page.html', {'products': products})


def confirmation_view(request: HttpRequest, order_id: Any):
    if request.method == 'POST':

        form = PaymentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            card_number = form.cleaned_data['card_number']
            expiration_at = form.cleaned_data['expiration_at']
            cvv_code = form.cleaned_data['cvv_code']
            order_type = form.cleaned_data['order_type']

            payment_data = {
                'name': name,
                'email': email,
                'card_number': card_number,
                'expiration_at': expiration_at,
                'cvv_code': cvv_code
            }

            # place for a payment API part where I send data to a bank
            # if I get 200 code about payment

            order = get_object_or_404(Order, pk=order_id)
            order.status = 'paid'
            order.order_type = order_type
            order.save()

            messages.success(
                request,
                'Payment completed successfully! 🎉 Your order is now paid.'
                )
            return redirect('home')

    order = get_object_or_404(Order, pk=order_id)
    form = PaymentForm()
    return render(request, 'shop/confirmation.html', {
        'order': order,
        'form': form
        })
