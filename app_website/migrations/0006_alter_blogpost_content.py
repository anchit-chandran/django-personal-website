# Generated by Django 4.2.1 on 2023-05-29 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_website', '0005_alter_blogpost_author_alter_blogpost_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(max_length=10000, null=True),
        ),
    ]
