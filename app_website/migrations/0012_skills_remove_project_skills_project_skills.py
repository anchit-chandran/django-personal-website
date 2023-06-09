# Generated by Django 4.2.1 on 2023-06-02 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_website', '0011_remove_project_meta_data_project_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='skills',
        ),
        migrations.AddField(
            model_name='project',
            name='skills',
            field=models.ManyToManyField(blank=True, to='app_website.skills'),
        ),
    ]
