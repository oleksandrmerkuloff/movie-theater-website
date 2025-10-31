from django.db import models
from movies.models import Movie
from django.utils import timezone

class Hall(models.Model):
    name = models.CharField(max_length=50)
    rows = models.PositiveIntegerField(default=10)
    seats_per_row = models.PositiveIntegerField(default=12)

    def __str__(self):
        return f"Hall {self.name} ({self.rows}×{self.seats_per_row})"


class Seat(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name="seats")
    row = models.PositiveIntegerField()
    number = models.PositiveIntegerField()

    class Meta:
        unique_together = ('hall', 'row', 'number')
        ordering = ['row', 'number']

    def __str__(self):
        return f"Row {self.row}, Seat {self.number}"


class MovieSession(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='sessions')
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='sessions')
    start_time = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.movie.name} in {self.hall.name} at {self.start_time.strftime('%Y-%m-%d %H:%M')}"


class SessionSeat(models.Model):
    STATUS_CHOICES = [
        ('free', 'Free'),
        ('reserved', 'Reserved'),
        ('sold', 'Sold'),
    ]

    session = models.ForeignKey(MovieSession, on_delete=models.CASCADE, related_name="session_seats")
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='free')

    class Meta:
        unique_together = ('session', 'seat')

    def __str__(self):
        return f"{self.session} - {self.seat} ({self.status})"
