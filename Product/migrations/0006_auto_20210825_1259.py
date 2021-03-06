# Generated by Django 3.2.5 on 2021-08-25 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0005_product_accessories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories '},
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='product', verbose_name='صوره المنتج'),
        ),
    ]
