# Generated by Django 4.1.7 on 2023-05-13 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise_web', '0025_productvariant'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='variant',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
