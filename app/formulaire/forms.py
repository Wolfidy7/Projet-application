from django import forms 

class SendWork(forms.Form):
    name = forms.CharField(required=True)
    file = forms.FileField()
    