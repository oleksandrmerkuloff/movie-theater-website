from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, render

from orders.models import Order
from accounts.models import User


def test_profile_view(request, pk):
    orders = Order.objects.filter(user=User)
    return render(request, 'accounts/profile.html', {'orders': orders})


def profile_view(request):
    user = request.user
    profile = user.profile  # Assuming OneToOneField
    orders = Order.objects.filter(user=user).prefetch_related('items__product')
    return render(request, 'account/profile.html', {'user': user, 'profile': profile, 'orders': orders})
