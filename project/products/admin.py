from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'purchase_price',
        'sale_price',
        'stock',
        'description',
    )

    fields = (
        'name',
        'purchase_price',
        'sale_price',
        'stock',
        'description',
        'created_at',
        'updated_at',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )
