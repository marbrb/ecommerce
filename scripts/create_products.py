from products.models import Product

l = []

for x in l:
    name, quantity, price = x.split("PERRITO")
    quantity = int(quantity.split()[-1])
    price = int(price.replace('.', '')[1:]) / quantity
    product = Product(
        name=name,
        purchase_price=price,
        sale_price=price*2,
        stock=quantity
    )
    product.save()
