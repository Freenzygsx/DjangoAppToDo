# Generated by Django 4.1.2 on 2022-10-16 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_tasks_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='user',
            new_name='user_id',
        ),
    ]