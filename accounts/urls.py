from django.urls import path

from accounts.views import (
    profile_view,
    logout_view,
    login_view,
    register_view
)


urlpatterns = [
    path('<uuid:pk>/', profile_view, name='test-profile'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]
