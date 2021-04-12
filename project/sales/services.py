from decimal import Decimal
from products.models import Product

def get_calculated_sale_values(products):
    total_sale_amount = Decimal(0)
    for product in products:
        total_sale_amount += \
            Decimal(product['sale_price']) * int(product['quantity'])

    total_purchase_amount = Decimal(0)
    for product in products:
        total_purchase_amount += \
            Decimal(product['purchase_price']) * int(product['quantity'])

    return total_purchase_amount, total_sale_amount


def update_stock(sale):
    products_dict = dict()
    for product in sale.products:
        products_dict[int(product['id'])] = product

    products = Product.objects.filter(id__in=list(products_dict.keys()))

    for product in products:
        product.stock -= int(products_dict[product.id]['quantity'])
        product.save()
