# Generated by Django 5.2 on 2025-05-29 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_remove_product_category_brand_slug_delete_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]
