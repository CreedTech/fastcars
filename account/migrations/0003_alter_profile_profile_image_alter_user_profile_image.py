# Generated by Django 4.0.6 on 2022-09-02 09:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_profile_profile_image_alter_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='portfolio/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='portfolio/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'jpeg'])]),
        ),
    ]
