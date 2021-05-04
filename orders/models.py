from django.db import models

from accounts.models import UserAccount
from products.models import Product


class OrderLine(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, name="product_in_order_lines")
    number_of_products = models.PositiveIntegerField()
    product_price = models.PositiveIntegerField()

    # order = models.ForeignKey(Order, on_delete=models.CASCADE, name="order_lines")

    def __str__(self):
        return f'{self.product}, {self.number_of_products}, {self.product_price}'


class Order(models.Model):
    username = models.CharField(max_length=128)
    total_cost = models.PositiveIntegerField()
    delivery_address = models.CharField(max_length=256)
    user_address = models.CharField(max_length=256)
    date_of_submission = models.DateTimeField()
    order_lines = models.ForeignKey(OrderLine, on_delete=models.CASCADE, name="order_lines_of_order")
    client = models.ForeignKey(UserAccount, on_delete=models.CASCADE, name="client_of_store")
    status_CHOICES = (
        ("PEND", "Pending"),
        ("PRO", "Processing"),
        ("DISPA", "Dispatched"),
        ("COMP", "Complete"),
        ("CANC", "Cancelled"),
        ("FAIL", "Failed"),
        ("DECL", "Declined"),
        ("REF", "Refunded"),
    )
    product_type = models.CharField(
        max_length=5,
        choices=status_CHOICES,
        default="PEND",
    )

    def __str__(self):
        return f'{self.user_address}, {self.total_cost}, {self.delivery_address}'
