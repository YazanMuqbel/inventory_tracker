# Generated by Django 2.2.4 on 2023-07-13 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0003_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]