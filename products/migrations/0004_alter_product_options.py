# Generated by Django 3.2 on 2021-10-08 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('special_status', 'Can read all products')]},
        ),
    ]
