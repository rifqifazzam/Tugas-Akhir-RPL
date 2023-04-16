# Generated by Django 4.1.7 on 2023-04-14 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise_web', '0006_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(to='merchandise_web.product'),
        ),
    ]