# Generated by Django 4.0.6 on 2022-09-03 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_alter_brand_options_brand_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Brand', 'verbose_name_plural': 'Brands'},
        ),
    ]