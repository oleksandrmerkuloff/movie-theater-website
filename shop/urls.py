from django.urls import path

from shop.views import shop_view, confirmation_view


urlpatterns = [
    path('', shop_view, name='shop'),
    path('confirm/<uuid:order_id>/', confirmation_view, name='confirm')
]
