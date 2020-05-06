# Generated by Django 2.2 on 2020-05-06 03:58

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='total_purchase_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19, verbose_name='Precio de compra'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sale',
            name='total_sale_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19, verbose_name='Precio de venta'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='sale',
            name='products',
        ),
        migrations.AddField(
            model_name='sale',
            name='products',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}, verbose_name='Productos vendidos'),
            preserve_default=False,
        ),
    ]