from django.urls import path

from accounts.views import ProfileView, ChangeView, DeleteView


urlpatterns = [
    path('profile/<uuid:pk>', ProfileView.as_view(), name='user-profile'),
    path('change/<uuid:pk>', ChangeView.as_view(), name='change-profile'),
    path('delete/<uuid:pk>', DeleteView.as_view(), name='delete-profile'),
]
