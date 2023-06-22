from django.db import models
import authentication.models
from django.contrib.staticfiles.storage import staticfiles_storage

class Subject(models.Model):
    
    '''def __str__(self):
        return f'{self.id_user}' '''
    
    @property
    def url(self):
        # Générer l'URL du fichier en utilisant le nom du fichier
        return staticfiles_storage.url(self.subject.name)
    SYSTEME='SYSTEME'
    GENTOO = 'GENTOO'
    RESEAU = 'RESEAU'
 
    CATEGORY_CHOICES = (
        (SYSTEME, 'TP_Systeme'),
        (GENTOO, 'TP_Gentoo'),
        (RESEAU, 'TP_Reseau')
    )

    
    id_user = models.ForeignKey(authentication.models.User,
                                on_delete=models.CASCADE)
    #username = models.CharField(max_length=150, null=True)
    subject = models.FileField(null=True, default=None, upload_to="data/subject_files/")
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