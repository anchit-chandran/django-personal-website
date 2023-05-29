# Generated by Django 4.2.1 on 2023-05-29 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_website', '0004_alter_blogpost_header_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='featured',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='posted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
