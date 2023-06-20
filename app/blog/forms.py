from django import forms

from . import models

class SubmitSubject(forms.ModelForm):
    
    class Meta:
        model = models.Subject
        fields = ['categorie', 'subject', 'correction']
        
        

class SubmitWork(forms.ModelForm):
    
    class Meta:
        model = models.Subject
        fields = ['categorie', 'devoir']
    