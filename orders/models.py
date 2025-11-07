from django.db import models
from django.contrib.auth import get_user_model

import uuid


User = get_user_model()


class Order(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_text = models.CharField(max_length=15, null=True)
    order_type = models.CharField(max_length=30, null=True)
    status = models.CharField(
        choices=[
            ('np', 'not paid'),
            ('paid', 'paid'),
            ('comp', 'completed')
        ],
        default='np',
        blank=True
    )

    def __str__(self) -> str:
        return f'{self.user} with {self.total_text}'


class OrderItem(models.Model):
    name = models.CharField(max_length=75)
    price_text = models.CharField(max_length=15, null=True)
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
        )

    def __str__(self) -> str:
        return f'{self.name}: {self.price_text}'
