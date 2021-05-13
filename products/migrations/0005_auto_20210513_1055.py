# Generated by Django 3.2 on 2021-05-13 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_products_under_category_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
