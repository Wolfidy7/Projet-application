# Generated by Django 4.2.2 on 2023-06-20 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_subject_categorie_resultat'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='devoir',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]