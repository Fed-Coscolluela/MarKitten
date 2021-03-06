# Generated by Django 4.0.4 on 2022-05-25 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markitten_app', '0007_alter_supplier_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'managed': False, 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='productarchive',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='supplierarchive',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='supplierproduct',
            options={'managed': False},
        ),
        migrations.AlterModelTable(
            name='supplier',
            table='Suppliers',
        ),
    ]
