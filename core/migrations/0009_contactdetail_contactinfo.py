# Generated by Django 4.0.6 on 2022-09-11 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_about_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Sam Smith', max_length=100)),
                ('email', models.EmailField(help_text='SS@gmail.com', max_length=254)),
                ('subject', models.CharField(help_text='Booking', max_length=100)),
                ('message', models.TextField(help_text='My name is...')),
            ],
            options={
                'verbose_name': 'Contact Detail',
                'verbose_name_plural': 'Contact Details',
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_icon', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Contact Info',
                'verbose_name_plural': 'Contact Information',
            },
        ),
    ]
