# Generated by Django 4.1.1 on 2022-09-22 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='description',
            new_name='header',
        ),
    ]