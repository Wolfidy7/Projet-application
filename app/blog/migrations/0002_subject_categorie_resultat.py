# Generated by Django 4.2.2 on 2023-06-20 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='categorie',
            field=models.CharField(choices=[('SYSTEME', 'TP_Systeme'), ('GENTOO', 'TP_Gentoo')], default='SYSTEME', max_length=30),
        ),
        migrations.CreateModel(
            name='Resultat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.IntegerField(default=-1)),
                ('id_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.subject')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
