# Generated by Django 3.2.24 on 2024-03-08 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_auto_20240308_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='is_new_release',
            field=models.BooleanField(default=False, verbose_name='Is New Release'),
        ),
    ]
