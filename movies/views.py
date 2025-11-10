from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.utils import timezone

from collections import defaultdict

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
    pk_url_kwarg = 'movie_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        today = timezone.now().date()
        sessions = self.object.movie_sessions.filter(  # ← ФИКС: movie_sessions
            start_time__date=today
        ).select_related('hall').order_by('hall__name', 'start_time')

        sessions_by_hall = defaultdict(list)
        for session in sessions:
            sessions_by_hall[session.hall.name].append(session)

        context['sessions_by_hall'] = dict(sessions_by_hall)
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
