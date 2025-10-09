from django.urls import path


from movies.views import HomePageView, DetailMovieView, SoonPageView, GenreView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path(
        'movie/<uuid:movie_id>/',
        DetailMovieView.as_view(),
        name='movie-detail'
        ),
    path('coming-soon/', SoonPageView.as_view(), name='coming-soon'),
    path(
        'genre/<str:genre_name>/',
        GenreView.as_view(),
        name='movies-by-genre'
        )
]
