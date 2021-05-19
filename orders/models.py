import datetime

from django.db import models

from accounts.models import UserAccount
from products.models import Product


class Order(models.Model):
    client = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="orders")
<<<<<<< HEAD
    date_of_submission = models.DateField()
    active = models.BooleanField()  # If active=True, it means an active basket but order wasn't made yet
    sum = models.DecimalField(max_digits=7, decimal_places=2)  # price of the whole order
=======
    date_of_submission = models.DateField(default=datetime.date.today)
    active = models.BooleanField()  # If active=True, it means an active basket but order wasn't made yet
    invoice_total = models.DecimalField(max_digits=7, decimal_places=2, default=0)  # price of the whole order
>>>>>>> feature/Order-Models
    STATUS_CHOICES = (
        ("NP", "Not Paid"),
        ("PD", "Paid"),
        ("SH", "Shipped"),
        ("DL", "Delivered")
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default="NP"
    )
<<<<<<< HEAD


class OrderLine(models.Model):
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    number_of_products = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)  # price of one line of order
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_lines")

    class Meta:
        unique_together = [
            ['product', 'order'],
        ]
=======

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f'OrderID: {self.pk} - User: {self.client}'


class OrderLine(models.Model):
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)  # price of one line of order
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_lines")

    def __str__(self):
        return f'{self.order} , {self.product} , {self.quantity} , {self.price}'
>>>>>>> feature/Order-Models
