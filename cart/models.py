from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

import uuid

from shop.models import Product


User = get_user_model()


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='carts'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user}\'s cart'

    @property
    def total(self):
        return sum(item.total for item in self.items.all())  # type: ignore


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField(
        default=1,
        validators=[
            MinValueValidator(1)
        ],
        null=False
    )
    price = models.PositiveIntegerField()

    @property
    def total(self):
        return self.price * self.quantity

    def __str__(self) -> str:
        return f'{self.product} in {self.cart}'

    def save(self, *args, **kwargs) -> None:
        if not self.price:
            self.price = self.product.price
        return super().save(*args, **kwargs)

    class Meta:
        unique_together = ('cart', 'product',)
