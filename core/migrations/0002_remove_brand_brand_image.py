# Generated by Django 4.0.6 on 2022-09-07 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='brand_image',
        ),
    ]
