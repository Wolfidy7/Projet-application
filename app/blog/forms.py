from django import forms

from . import models

class SubmitSubject(forms.ModelForm):
    
    class Meta:
        model = models.Subject
        fields = ['subject', 'correction', 'categorie']
        
        

class SubmitWork(forms.ModelForm):
    
    class Meta:
        model = models.Subject
        fields = []
    