# Generated by Django 2.0.3 on 2018-05-18 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_auto_20180518_1023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bannerslider',
            old_name='product_id',
            new_name='productId',
        ),
    ]