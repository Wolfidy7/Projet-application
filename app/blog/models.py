from django.db import models
import authentication.models


class Subject(models.Model):
    
    '''def __str__(self):
        return f'{self.id_user}' '''
    
    
    SYSTEME='SYSTEME'
    GENTOO = 'GENTOO'
 
    CATEGORY_CHOICES = (
        (SYSTEME, 'TP_Systeme'),
        (GENTOO, 'TP_Gentoo'),
    )

    
    id_user = models.ForeignKey(authentication.models.User,
                                on_delete=models.CASCADE)
    #username = models.CharField(max_length=150, null=True)
    subject = models.FileField(null=True, default=None)
    categorie = models.CharField(choices=CATEGORY_CHOICES, max_length=30, default=SYSTEME)
    correction = models.FileField(upload_to="data/corrections/")
    
    devoir = models.FileField(null=True, upload_to="data/devoirs/")

class Resultat(models.Model):
    
    def __str__(self):
        return f'{self.id_user}'
    id_user = models.ForeignKey(authentication.models.User,
                                on_delete=models.CASCADE)
    id_subject = models.ForeignKey(Subject,
                                   on_delete=models.CASCADE)
    
    note= models.IntegerField(default=-1)