from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.utils import timezone

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
    pk_url_kwarg = 'movie_id'  # ← tells Django to use movie_id from URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        today = timezone.now().date()
        context['sessions_today'] = self.object.sessions.filter(
            start_time__date=today
        ).order_by('start_time')

        return context


class MoviesListView(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'movies/movies-list.html'

    def get_queryset(self) -> QuerySet[Any]:
        return Movie.objects.filter(in_theater=True)


def soon_page(request):
    dates = Movie.objects.filter(in_theater=False).values_list(
        'release_at', flat=True
        )
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


def about_view(request):
    return render(request, 'movies/about.html')
