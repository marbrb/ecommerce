from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Nombre'
    )

    purchase_price = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name='Precio de compra',
        help_text='Precio por unidad al por mayor'
    )

    sale_price = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name='Precio de venta',
        help_text='Precio por unidad al detal'
    )

    stock = models.IntegerField(
        verbose_name='Número de productos disponibles',
        default=0
    )

    description = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        verbose_name='Descripción'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de creación',
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Fecha de última actualización',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
