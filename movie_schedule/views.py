from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import json

from movie_schedule.models import Session, Seat
from movie_schedule.forms import TicketPaymentForm
from orders.models import Order, OrderItem


@login_required
def ticket_checkout_view(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    cart = request.session.get('ticket_cart', [])

    if not cart:
        messages.error(request, "Your cart is empty.")
        return redirect('hall', session_id=session_id)

    total = sum(item['price'] for item in cart)

    if request.method == 'POST':
        request.session['ticket_order_data'] = {
            'session_id': session_id,
            'seats': cart,
            'total': total
        }
        return redirect('ticket_payment')

    context = {
        'session': session,
        'cart': cart,
        'total': total,
    }
    return render(request, 'movie_schedule/ticket_checkout.html', context)


@login_required
def ticket_payment_view(request):
    order_data = request.session.get('ticket_order_data')
    if not order_data:
        return redirect('hall', session_id=1)

    session = get_object_or_404(Session, id=order_data['session_id'])
    cart = order_data['seats']
    total = order_data['total']

    if request.method == 'POST':
        form = TicketPaymentForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                user=request.user,
                total_text=f'{total} UAH',
                order_type='movie_ticket',
                status='paid'
            )

            for item in cart:
                seat_name = f'R{item["row"]}-S{item["seat"]}'

                OrderItem.objects.create(
                    order=order,
                    name=seat_name,
                    price_text=f'{item["price"]} UAH',
                    quantity=1
                )

                seat = get_object_or_404(Seat, id=item['seat_id'], session=session)
                seat.is_booked = True
                seat.save()

            request.session.pop('ticket_cart', None)
            request.session.pop('ticket_order_data', None)

            messages.success(
                request,
                f'Payment successful! Tickets for «{session.movie.name}» booked.'
            )
            return redirect('ticket_success')
        else:
            print('FORM ERRORS:', form.errors)
            messages.error(request, 'Correct the errors in the form.')
    else:
        form = TicketPaymentForm()

    context = {
        'session': session,
        'cart': cart,
        'total': total,
        'form': form,
    }
    return render(request, 'movie_schedule/ticket_payment.html', context)


@login_required
def ticket_success_view(request):
    return render(request, 'movie_schedule/ticket_success.html')


@login_required
def hall_view(request, session_id):
    session = get_object_or_404(Session, id=session_id)

    if 'ticket_cart' in request.GET:
        try:
            cart_data = json.loads(request.GET['ticket_cart'])
            request.session['ticket_cart'] = cart_data
            request.session.modified = True
        except Exception:
            pass

    if request.method == 'POST':
        if 'clear_cart' in request.POST:
            request.session['ticket_cart'] = []
            request.session.modified = True
            return redirect('hall', session_id=session_id)
        elif 'proceed_to_payment' in request.POST:
            try:
                cart_data = json.loads(request.POST.get('ticket_cart', '[]'))
                request.session['ticket_cart'] = cart_data
                request.session.modified = True
            except json.JSONDecodeError:
                pass
            return redirect('ticket_checkout', session_id=session_id)

    cart = request.session.get('ticket_cart', [])
    selected_seat_ids = [item['seat_id'] for item in cart if 'seat_id' in item]

    context = {
        'session': session,
        'cart': cart,
        'total_price': sum(item['price'] for item in cart),
        'selected_seat_ids': selected_seat_ids,
    }
    return render(request, 'movie_schedule/hall.html', context)
