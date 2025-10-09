from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

import uuid
from decimal import Decimal


class BasePersonModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    first_name = models.CharField(
        max_length=30
    )
    last_name = models.CharField(
        max_length=40
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def amount_of_movies(self):
        return self.movies.count()  # type: ignore

    def __str__(self) -> str:
        return self.full_name

    def __repr__(self) -> str:
        return f'{self.full_name} has {self.amount_of_movies}'

    class Meta:
        ordering = ('-last_name',)
        abstract = True


class Director(BasePersonModel):
    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directors'


class Actor(BasePersonModel):
    class Meta:
        verbose_name = 'Actor'
        verbose_name_plural = 'Actors'


class Screenwriter(BasePersonModel):
    class Meta:
        verbose_name = 'Screenwriter'
        verbose_name_plural = 'Screenwriters'


class BaseSupportMovieModel(models.Model):
    name = models.CharField(
        unique=True,
        max_length=70
    )

    @property
    def movie_count(self):
        return self.movies.count()  # type: ignore

    def __str__(self) -> str:
        return self.name

    class Meta:
        abstract = True


class Language(BaseSupportMovieModel):
    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'


class Genre(BaseSupportMovieModel):
    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Country(BaseSupportMovieModel):
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class Studio(BaseSupportMovieModel):
    class Meta:
        verbose_name = 'Studio'
        verbose_name_plural = 'Studios'


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name='movie name'
    )
    age_restrictions = models.PositiveIntegerField(
        blank=False,
        null=False,
        verbose_name='age restrictions',
        validators=[
            MinValueValidator(0),
        ]
    )
    poster = models.ImageField(
        upload_to='posters/%Y/%m/',
        blank=True,
        null=True
        )
    trailer_link = models.URLField(
        verbose_name='trailer',
        blank=True,
        null=True
    )
    year = models.CharField(
        max_length=5,
        null=True,
        blank=True
    )
    release_at = models.DateField(
        blank=True,
        null=True
    )
    in_theater = models.BooleanField(
        blank=True,
        default=False
    )
    original_name = models.CharField(
        max_length=100,
        blank=True,
    )
    director = models.ForeignKey(
        Director,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='movies'
    )
    language = models.ForeignKey(
        Language,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='movies'
    )
    viewer_rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        blank=True,
        default=Decimal('0.00'),
        validators=[
            MinValueValidator(Decimal('0.00')),
            MaxValueValidator(Decimal('10.00'))
        ]
    )
    critics_rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        blank=True,
        default=Decimal('0.00'),
        validators=[
            MinValueValidator(Decimal('0.00')),
            MaxValueValidator(Decimal('10.00'))
        ]
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        related_name='movies',
    )
    duration = models.DecimalField(
        max_digits=2,
        decimal_places=2,
        blank=True,
        default=Decimal('0.00')
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='movies'
    )
    studio = models.ForeignKey(
        Studio,
        on_delete=models.CASCADE,
        related_name='movies',
    )
    screenplay = models.ManyToManyField(
        Screenwriter,
        blank=True,
        related_name='movies',
    )
    starring = models.ManyToManyField(
        Actor,
        blank=True,
        related_name='movies',
    )
    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'{self.name} by {self.director or 'Unknown Director'}'

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        ordering = ('-release_at', 'name', 'in_theater')
