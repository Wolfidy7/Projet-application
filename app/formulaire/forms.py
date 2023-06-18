from django import forms 
from .models import Data

class SendWork(forms.ModelForm):
    
    class Meta:
        model = Data
        fields = ['name', 'file']
        
  

    