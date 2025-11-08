from django.urls import path

from movie_schedule import views


urlpatterns = [
    path('movie/<int:movie_id>/', views.session_list, name='session_list'),
    path('hall/<int:session_id>/', views.hall_view, name='hall'),
]
