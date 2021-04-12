from decimal import Decimal
import json

from django import forms

from .models import Sale


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = (
            'products',
        )
