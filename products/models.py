from enum import Enum
from django.db import models
from django.db.models import IntegerField
from accounts.models import Author
# The connection is bad


class Category(models.Model):
    name = models.CharField(max_length=128)
    # parent categories and 'children'categories(tree placement)

    def __str__(self):
        return f'{self.name}'



class Product(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    #thumbnail =
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, name="products_under_category")
    price = IntegerField()
    
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




