from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    PROFESSOR = 'PROFESSOR'
    STUDENT = 'STUDENT'

    ROLE_CHOICES = (
        (PROFESSOR, 'Professeur'),
        (STUDENT, 'Etudiant'),
    )
    profile_photo = models.ImageField(verbose_name='photo de profil', null=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='rôle')
    
    