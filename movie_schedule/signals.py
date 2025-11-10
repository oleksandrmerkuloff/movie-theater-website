from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Session, Seat


@receiver(post_save, sender=Session)
def create_hall_seats(sender, instance, created, **kwargs):
    if created:
        seats = []
        for row in range(1, 11):  # 1..10
            for col in range(1, 11):
                is_premium = row > 8  # 9 и 10 — премиум
                seats.append(
                    Seat(
                        session=instance,
                        row=row,
                        seat=col,
                        is_booked=False,
                        is_premium=is_premium
                    )
                )
        Seat.objects.bulk_create(seats)
