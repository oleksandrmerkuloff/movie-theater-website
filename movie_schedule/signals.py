from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Session, Seat


@receiver(post_save, sender=Session)
def create_seats(sender, instance, created, **kwargs):
    if created:
        for row in range(1, instance.hall.rows + 1):
            for seat_num in range(1, instance.hall.seats_per_row + 1):
                is_premium = row > (instance.hall.rows - 2)
                Seat.objects.create(
                    session=instance,
                    row=row,
                    seat=seat_num,
                    is_premium=is_premium
                )
