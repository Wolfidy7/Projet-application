# Generated by Django 4.2.2 on 2023-06-21 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_remove_user_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_photo',
        ),
    ]
