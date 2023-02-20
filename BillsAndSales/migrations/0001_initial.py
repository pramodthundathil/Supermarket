# Generated by Django 3.2.14 on 2023-01-11 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_products_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillCalculations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=11)),
                ('gst', models.CharField(max_length=100, null=True)),
                ('totalprice', models.CharField(max_length=100, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
        ),
    ]