# Generated by Django 3.0.3 on 2021-04-10 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tasks',
            new_name='Task',
        ),
    ]