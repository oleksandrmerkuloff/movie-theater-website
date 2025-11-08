from django.db import models
from django.core.exceptions import ValidationError

from decimal import Decimal
from datetime import datetime

from movies.models import Movie


class Hall(models.Model):
    name = models.CharField(max_length=50)
    rows = models.IntegerField(default=10)
    seats_per_row = models.IntegerField(default=10)

    def __str__(self):
        return self.name


class Session(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='sessions'
        )
    hall = models.ForeignKey(
        Hall,
        on_delete=models.CASCADE
        )
    start_time = models.DateTimeField()
    price_standard = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=Decimal(150.00)
        )
    price_premium = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=Decimal(250.00)
        )

    class Meta:
        unique_together = ('hall', 'start_time')

    def __str__(self):
        return f"{self.movie.name} - {self.start_time.strftime('%Y-%m-%d %H:%M')}"

    def clean(self):
        if self.start_time < datetime.now():
            raise ValidationError("Cannot create session in the past.")


class Seat(models.Model):
    session = models.ForeignKey(
        Session,
        on_delete=models.CASCADE,
        related_name='seats'
        )
    row = models.IntegerField()
    seat = models.IntegerField()
    is_booked = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)

    class Meta:
        unique_together = ('session', 'row', 'seat')

    def __str__(self):
        return f"R{self.row}-S{self.seat} ({'Premium' if self.is_premium else 'Standard'})"
