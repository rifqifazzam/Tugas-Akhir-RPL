# Generated by Django 4.1.7 on 2023-04-21 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise_web', '0006_remove_product_digital'),
    ]

    operations = [
        migrations.AddField(
            model_name='expedition',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/expedition/'),
        ),
        migrations.AddField(
            model_name='expedition',
            name='price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='expedition',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]