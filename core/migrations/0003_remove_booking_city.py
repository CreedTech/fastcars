# Generated by Django 4.0.6 on 2022-09-09 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_brand_brand_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='city',
        ),
    ]