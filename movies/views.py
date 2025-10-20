from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from movies.models import Movie


class HomePageView(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'movies/index.html'

    def get_queryset(self) -> QuerySet[Any]:
        return Movie.objects.filter(in_theater=True)


class DetailMovieView(DetailView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'movie-page.html'

    def get_object(self) -> Model:
        movie_id = self.kwargs.get('movie_id')
        return get_object_or_404(Movie, id=movie_id)


class SoonPageView(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'soon-page.html'

    def get_queryset(self) -> QuerySet[Any]:
        return Movie.objects.filter(in_theater=False)


class GenreView(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'genre-list.html'

    def get_queryset(self) -> QuerySet[Any]:
        genre_name = self.kwargs.get('genre_name')
        return Movie.objects.filter(genres__name__iexact=genre_name).distinct()
