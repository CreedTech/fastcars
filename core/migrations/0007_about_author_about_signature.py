# Generated by Django 4.0.6 on 2022-09-11 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='author',
            field=models.CharField(default='LazyProgrammer', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='signature',
            field=models.CharField(default='fastcars', max_length=50),
            preserve_default=False,
        ),
    ]