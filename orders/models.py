from django.db import models
from django.contrib.auth import get_user_model

import uuid


User = get_user_model()


class Order(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        choices=[
            ('paid', 'paid'),
            ('comp', 'completed')
        ],
        default='paid'
    )


class OrderItem(models.Model):
    name = models.CharField(max_length=75)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
