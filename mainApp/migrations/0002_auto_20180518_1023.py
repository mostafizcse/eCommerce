# Generated by Django 2.0.3 on 2018-05-18 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bannerslider',
            old_name='product',
            new_name='product_id',
        ),
    ]
