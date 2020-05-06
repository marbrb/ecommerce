from django.contrib.postgres.fields import JSONField
from django.db import models


class Sale(models.Model):
    # it should have this keys:
    #   - id
    #   - quantity
    #   - purchase_amount
    #   - sale_amount
    products = JSONField(
        verbose_name='Productos vendidos'
    )

    total_sale_amount = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name='Precio de venta',
    )

    total_purchase_amount = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name='Precio de compra',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de creación',
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Fecha de última actualización',
    )

    @property
    def revenue(self):
        return self.total_sale_amount - self.total_purchase_amount

    def __str__(self):
        return "Venta {}".format(self.id)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
