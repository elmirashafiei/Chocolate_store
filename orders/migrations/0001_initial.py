# Generated by Django 3.2 on 2021-05-04 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_auto_20210504_1502'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_products', models.PositiveIntegerField()),
                ('product_price', models.PositiveIntegerField()),
                ('product_in_order_lines', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128)),
                ('total_cost', models.PositiveIntegerField()),
                ('delivery_address', models.CharField(max_length=256)),
                ('user_address', models.CharField(max_length=256)),
                ('date_of_submission', models.DateTimeField()),
                ('product_type', models.CharField(choices=[('PEND', 'Pending'), ('PRO', 'Processing'), ('DISPA', 'Dispatched'), ('COMP', 'Complete'), ('CANC', 'Cancelled'), ('FAIL', 'Failed'), ('DECL', 'Declined'), ('REF', 'Refunded')], default='PEND', max_length=5)),
                ('client_of_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.useraccount')),
                ('order_lines_of_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.orderline')),
            ],
        ),
    ]