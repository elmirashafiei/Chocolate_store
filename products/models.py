from django.db import models
from django.db.models import DecimalField

from accounts.models import Author


# The connection is bad


class Category(models.Model):
    name = models.CharField(max_length=128)
    thumbnail = models.ImageField(upload_to="images/")



    # parent categories and 'children'categories(tree placement)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    thumbnail = models.ImageField(upload_to="images/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = DecimalField(max_digits=10, decimal_places=2)
    PRODUCT_TYPES_CHOICES = (
        ("SUBS", "Subscription to a service"),
        ("ITEM", "Item shipped to the customer")
    )
    product_type = models.CharField(
        max_length=4,
        choices=PRODUCT_TYPES_CHOICES,
        default="ITEM",
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, name="products_of_author")

    def __str__(self):
        return f'{self.title} , {self.price} , {self.category}'


 #class ImagesPro(models.Model):

