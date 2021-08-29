# Generated by Django 3.2.5 on 2021-08-29 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0008_product_discountprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_bestseller',
            field=models.BooleanField(default=True, verbose_name='هل المنتج احسن مبيعات ؟'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_new',
            field=models.BooleanField(default=True, verbose_name='هل المنتج جديد ؟'),
        ),
    ]