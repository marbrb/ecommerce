from django.contrib import admin

from .models import Sale


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
    )

    fields = (
        'products',
        'created_at',
        'updated_at',
    )

    readonly_fields = (
        'products',
        'created_at',
        'updated_at',
    )
