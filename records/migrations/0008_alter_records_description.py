# Generated by Django 3.2.24 on 2024-03-14 10:07

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0007_rename_release_date_records_releasedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]