from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from .models import Session, Seat
from shop.forms import PaymentForm  # reuse


def session_list(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    today = timezone.now().date()
    sessions = Session.objects.filter(movie=movie, start_time__date=today)
    return render(request, 'sessions/session_list.html', {'movie': movie, 'sessions': sessions})


def hall_view(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    cart = request.session.get('cart', [])
    selected_seats = [f"R{r}-S{s}" for r, s in cart]

    if request.method == 'POST':
        if 'clear_cart' in request.POST:
            request.session['cart'] = []
            return redirect('sessions:hall', session_id=session_id)

        if 'proceed_payment' in request.POST and cart:
            request.session['order_type'] = 'ticket'
            request.session['ticket_seats'] = cart
            return redirect('store:payment')

    context = {
        'session': session,
        'selected_seats': selected_seats,
        'cart': cart,
    }
    return render(request, 'sessions/hall.html', context)
