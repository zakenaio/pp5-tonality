# Generated by Django 3.2.24 on 2024-03-11 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('answer', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'FAQs',
                'ordering': ['question'],
            },
        ),
    ]