from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    
    PROFESSOR = 'PROFESSOR'
    STUDENT = 'STUDENT'
    
    ROLES_CHOICES =(
        (PROFESSOR, 'Professeur'),
        (STUDENT, 'Etudiant'),
    )
    
    profile_photo = models.ImageField()
    role = models.CharField(max_length=30, choices=ROLES_CHOICES)
    