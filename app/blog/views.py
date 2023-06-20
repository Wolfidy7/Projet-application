from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import forms, models

@login_required
def home(request):
    return render(request, 'blog/home.html')




def submitSubject(request):
    
    form = forms.SubmitSubject
    return render(request, 'blog/p_submit.html',
                  context={'formu': form})
