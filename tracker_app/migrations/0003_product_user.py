# Generated by Django 2.2.4 on 2023-07-13 23:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='tracker_app.User'),
            preserve_default=False,
        ),
    ]