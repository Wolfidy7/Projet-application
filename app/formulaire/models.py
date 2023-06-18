from django.db import models

class Data(models.Model):
    
    def __str__(self):
        return f'{self.name}'
    name= models.CharField(max_length=100)
    file = models.FileField(upload_to="files")
    