# Generated by Django 4.2.1 on 2023-06-07 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_website', '0019_remove_project_header_img_path_project_header_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='posted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
