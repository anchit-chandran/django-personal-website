# Generated by Django 4.2.1 on 2023-06-02 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_website', '0014_rename_skills_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.ManyToManyField(blank=True, default='Newsletter', to='app_website.category'),
        ),
    ]
