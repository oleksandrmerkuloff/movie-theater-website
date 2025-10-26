from django.urls import path


from movies.views import (
    HomePageView, DetailMovieView, MoviesListView,
    soon_page, genre_view
    )


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path(
        'movie/<uuid:movie_id>/',
        DetailMovieView.as_view(),
        name='movie-detail'
        ),
    path('now-in-cinema/', MoviesListView.as_view(), name='now-in-cinema'),
    path('coming-soon/', soon_page, name='coming-soon'),
    path(
        'genre/<str:genre_name>/',
        genre_view,
        name='movies-by-genre'
        )
]
