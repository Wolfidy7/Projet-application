from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . import forms, models
from blog.models import *
@login_required
def home(request):
    return render(request, 'blog/home.html')




def submitSubject(request):
    
    form = forms.SubmitSubject(request.POST, request.FILES)
    if request.method =='POST':
        form = forms.SubmitSubject(request.POST)
        
        if form.is_valid():
            sujet = request.FILES['subject']
            correction = request.FILES['correction']
            categorie = form.cleaned_data['categorie']
            data = Subject(subject=sujet, correction=correction, categorie=categorie)
            #data.save()
            return redirect('redirection')
    else:
        form = forms.SubmitSubject()
    return render(request, 'blog/p_submit.html',
                  context={'formu': form})
    
def submitWork(request):
    pass


def p_redirect(request):
    
    return render(request, 'blog/redirect.html')