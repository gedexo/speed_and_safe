# Generated by Django 5.2 on 2025-06-06 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_remove_product_quantity_remove_productcategory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.FileField(null=True, upload_to='banners/'),
        ),
    ]
