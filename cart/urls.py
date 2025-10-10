from django.urls import path

from cart.views import CartView


urlpatterns = [
    path('<uuid:pk>/', CartView.as_view(), name='cart_page'),
]
