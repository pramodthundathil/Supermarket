# Generated by Django 3.2.14 on 2023-04-11 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BillsAndSales', '0007_alter_billid_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]