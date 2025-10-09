from django.contrib import admin

from movies.models import (
    Actor, Country, Director, Genre,
    Language, Movie, Screenwriter, Studio
)


class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                'fields': [
                    'name',
                    'age_restrictions',
                    'year',
                    'release_at',
                    'original_name',
                    'duration',
                    'description',
                    'in_theater'
                    ]
            }
        ),
        (
            'Media',
            {
                'classes': ['wide'],
                'fields': ['poster', 'trailer_link']
            }
        ),
        (
            'Additional data',
            {
                'classes': ['collapse'],
                'fields': [
                    'director',
                    'language',
                    'genre',
                    'country',
                    'studio',
                    'screenplay',
                    'starring'
                    ]
            }
        )
    ]
    list_display = ['name', 'year', 'in_theater', 'studio']
    list_editable = ['in_theater',]
    list_filter = [
        'age_restrictions',
        'year',
        'in_theater',
        'director',
        'genre',
        'country',
        'studio'
        ]
    list_per_page = 30
    readonly_fields = ['id', 'viewer_rating', 'critics_rating']
    search_fields = [
        'name', 'director__full_name', 'original_name', 'studio__name'
    ]
    autocomplete_fields = [
        'director',
        'language',
        'genre',
        'country',
        'studio',
        'screenplay',
        'starring'
        ]


admin.site.register(Actor)
admin.site.register(Country)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Screenwriter)
admin.site.register(Studio)
