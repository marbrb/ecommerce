from decimal import Decimal
import json

from django import forms

from .models import Sale


class SaleForm(forms.ModelForm):
    products = forms.CharField()

    total_sale_amount = forms.DecimalField(required=False)

    total_purchase_amount = forms.DecimalField(required=False)

    def clean_total_sale_amount(self):
        products = self.cleaned_data['products']
        total_sale_amount = Decimal(0)
        for product in products['products']:
            total_sale_amount += Decimal(product['sale_amount'])

        return total_sale_amount

    def clean_total_purchase_amount(self):
        products = self.cleaned_data['products']
        total_purchase_amount = Decimal(0)
        for product in products['products']:
            total_purchase_amount += Decimal(product['sale_amount'])

        return total_purchase_amount

    def clean_products(self):
        products = self.cleaned_data['products']
        try:
            products = json.loads(products)
        except json.decoder.JSONDecodeError:
            raise forms.ValidationError("Error en la aplicación")

        return products

    class Meta:
        model = Sale
        fields = (
            'products',
            'total_sale_amount',
            'total_purchase_amount',
        )
