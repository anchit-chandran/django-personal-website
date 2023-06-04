# Generated by Django 4.2.1 on 2023-06-04 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_website', '0018_project_header_img_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='header_img_path',
        ),
        migrations.AddField(
            model_name='project',
            name='header_img',
            field=models.URLField(default='https://images.unsplash.com/photo-1559291001-693fb9166cba?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80', max_length=500, null=True),
        ),
    ]
