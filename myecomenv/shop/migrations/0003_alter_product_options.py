# Generated by Django 4.2.1 on 2023-08-03 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_product"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ("name",),
                "verbose_name": "product",
                "verbose_name_plural": "products",
            },
        ),
    ]
