from django.apps import AppConfig


class MovieScheduleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movie_schedule'

    def ready(self):
        import movie_schedule.signals
