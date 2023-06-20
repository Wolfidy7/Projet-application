from django.db import models


class Subject(models.Model):
    
    subject = models.FileField()
    correction = models.FileField()
    