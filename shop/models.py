from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=75,
        unique=True
    )
    in_stock = models.BooleanField(
        default=False,
        blank=True
    )
    price = models.PositiveIntegerField(
        default=0,
        blank=True
    )
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name',]
