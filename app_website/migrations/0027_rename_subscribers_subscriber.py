# Generated by Django 4.2.1 on 2023-06-09 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_website', '0026_subscribers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscribers',
            new_name='Subscriber',
        ),
    ]
