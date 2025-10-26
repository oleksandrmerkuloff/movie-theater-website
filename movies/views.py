from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render

from movies.models import Movie


class HomePageView(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'movies/index.html'

    def get_queryset(self) -> QuerySet[Any]:
        return Movie.objects.filter(in_theater=True)[:4]


class DetailMovieView(DetailView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'movies/movie-page.html'

    def get_object(self) -> Model:
        movie_id = self.kwargs.get('movie_id')
        return get_object_or_404(Movie, id=movie_id)


class MoviesListView(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'movies/movies-list.html'

    def get_queryset(self) -> QuerySet[Any]:
        return Movie.objects.filter(in_theater=True)


def soon_page(request):
    dates = Movie.objects.filter(in_theater=False).values_list('release_at', flat=True)
    movies = Movie.objects.filter(in_theater=False)
    data = {
        'dates': sorted(set(dates)),
        'movies': movies
    }
    return render(request, 'movies/soon-page.html', data)


def genre_view(request, genre_name):
    movies = Movie.objects.filter(genre__name__iexact=genre_name).distinct()
    data = {'movies': movies, 'genre_name': genre_name}
    return render(request, 'movies/genre-list.html', data)

# class GenreView(ListView):
#     model = Movie
#     context_object_name = 'movies'
#     template_name = 'movies/genre-list.html'

#     def get_queryset(self) -> dict[str, Any]:
#         genre_name = self.kwargs.get('genre_name')
#         print(genre_name)
#         movies = Movie.objects.filter(genre__name__iexact=genre_name).distinct()
#         return {'movies': movies, 'genre_name': genre_name}
