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
    #username = models.CharField(max_length=150, null=True)
    subject = models.FileField()
    correction = models.FileField(upload_to="data/corrections/")
    categorie = models.CharField(choices=CATEGORY_CHOICES, max_length=30, default=SYSTEME)
    devoir = models.FileField(null=True, upload_to="data/devoirs/")

class Resultat(models.Model):
    
    id_user = models.ForeignKey(authentication.models.User,
                                on_delete=models.CASCADE)
    id_subject = models.ForeignKey(Subject,
                                   on_delete=models.CASCADE)
    
    note= models.IntegerField(default=-1)