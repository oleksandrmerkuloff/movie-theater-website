from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MovieSession, SessionSeat

@receiver(post_save, sender=MovieSession)
def create_session_seats(sender, instance, created, **kwargs):
    if created:
        seats = instance.hall.seats.all()
        SessionSeat.objects.bulk_create([
            SessionSeat(session=instance, seat=s, status='free')
            for s in seats
        ])
