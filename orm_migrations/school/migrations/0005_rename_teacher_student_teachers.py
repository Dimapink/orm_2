# Generated by Django 5.1 on 2024-08-27 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_rename_teacher_teachers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teacher',
            new_name='teachers',
        ),
    ]
