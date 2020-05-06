# Generated by Django 2.2 on 2020-05-06 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Nombre')),
                ('purchase_price', models.DecimalField(decimal_places=2, help_text='Precio por unidad al por mayor', max_digits=19, verbose_name='Precio de compra')),
                ('sale_price', models.DecimalField(decimal_places=2, help_text='Precio por unidad al detal', max_digits=19, verbose_name='Precio de venta')),
                ('stock', models.IntegerField(default=0, verbose_name='Número de productos disponibles')),
                ('description', models.CharField(blank=True, max_length=512, null=True, verbose_name='Descripción')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de última actualización')),
            ],
        ),
    ]