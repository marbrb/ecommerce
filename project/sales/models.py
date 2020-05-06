from django.db import models


class Sale(models.Model):
    products = models.ManyToManyField(
        'products.Product',
        related_name='sales',
        verbose_name='Productos'
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
    def total_sale_amount(self):
        total = 0
        for product in self.products.all():
            total += product.sale_price
        return total

    @property
    def total_purchase_amount(self):
        total = 0
        for product in self.products.all():
            total += product.purchase_price
        return total

    @property
    def revenue(self):
        return self.total_sale_amount - self.total_purchase_amount

    def __str__(self):
        return "Venta {}".format(self.id)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
