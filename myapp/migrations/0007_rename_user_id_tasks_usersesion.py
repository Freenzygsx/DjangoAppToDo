# Generated by Django 4.1.2 on 2022-10-16 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_user_tasks_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='user_id',
            new_name='usersesion',
        ),
    ]
