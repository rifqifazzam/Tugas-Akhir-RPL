# Generated by Django 4.1.7 on 2023-04-13 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise_web', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Categorie',
        ),
        migrations.RenameModel(
            old_name='Expeditions',
            new_name='Expedition',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
