from django.urls import path

from accounts.views import test_profile_view


urlpatterns = [
    path('<uuid:pk>/', test_profile_view, name='test-profile')
]
