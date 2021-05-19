from products.models import Product
from .models import OrderLine


def add_item_to_order(active_order, product_id, product_quantity):
    if OrderLine.objects.filter(order=active_order, product=product_id).exists():
        order_item = OrderLine.objects.get(
            order=active_order,
            product=Product.objects.get(id=product_id)
        )
        order_item.quantity += product_quantity
        order_item.save()

    else:
        OrderLine.objects.create(
            order=active_order,
            product=Product.objects.get(id=product_id),
            quantity=product_quantity,
            price=Product.objects.get(id=product_id).price
        )


def remove_item_from_order(active_order, product_id):
    order_item = OrderLine.objects.get(order=active_order, product=product_id)
    order_item.delete()


def update_item_in_order(active_order, product_id, product_quantity):
    order_item = OrderLine.objects.get(order=active_order, product=product_id)
    order_item.quantity = product_quantity
    order_item.save()
