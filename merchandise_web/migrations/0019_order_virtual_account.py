# Generated by Django 4.1.7 on 2023-04-29 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise_web', '0018_shipment_tracking_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='virtual_account',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
