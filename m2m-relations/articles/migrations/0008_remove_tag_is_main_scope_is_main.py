# Generated by Django 5.1 on 2024-08-29 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_remove_scope_is_main_tag_is_main_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='is_main',
        ),
        migrations.AddField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
