from django.views.generic import DetailView

from cart.models import Cart


class CartView(DetailView):
    model = Cart
    context_object_name = 'cart'
    template_name = 'cart-page.html'
