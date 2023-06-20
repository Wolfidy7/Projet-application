from django.db import models
import authentication.models

class Subject(models.Model):
    
    SYSTEME='SYSTEME'
    GENTOO = 'GENTOO'
 
    CATEGORY_CHOICES = (
        (SYSTEME, 'TP_Systeme'),
        (GENTOO, 'TP_Gentoo'),
    )
       
    id_user = models.ForeignKey(authentication.models.User,
                                on_delete=models.CASCADE)
    subject = models.FileField()
    correction = models.FileField()
    categorie = models.CharField(choices=CATEGORY_CHOICES, max_length=30, default=SYSTEME)
    

class Resultat(models.Model):
    
    id_user = models.ForeignKey(authentication.models.User,
                                on_delete=models.CASCADE)
    id_subject = models.ForeignKey(Subject,
                                   on_delete=models.CASCADE)
    
    note= models.IntegerField(default=-1)