# Generated by Django 4.2.2 on 2023-06-22 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_subject_correction_alter_subject_devoir'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject',
            field=models.FileField(default=None, null=True, upload_to='subject_files/'),
        ),
    ]
