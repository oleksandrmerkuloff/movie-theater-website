from django.urls import path

from movie_schedule import views


urlpatterns = [
    path('<int:session_id>/', views.hall_view, name='hall'),
    path('checkout/<int:session_id>/', views.ticket_checkout_view, name='ticket_checkout'),
    path('payment/', views.ticket_payment_view, name='ticket_payment'),
    path('success/', views.ticket_success_view, name='ticket_success'),
]
