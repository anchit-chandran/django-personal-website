# Generated by Django 4.2.1 on 2023-06-07 17:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_website', '0022_remove_blogpost_category_delete_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='posted_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
