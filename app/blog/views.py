from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . import forms, models
from blog.models import *
from blog.test.compare import *
from blog.compilation import *


@login_required
def home(request):
    return render(request, 'blog/home.html')


@login_required
def submitSubject(request):
    
    form = forms.SubmitSubject(request.POST, request.FILES)
    print("ok")
    if request.method =='POST':
        print("post ok")
        form = forms.SubmitSubject(request.POST, request.FILES)
        
        if form.is_valid():
            sujet = request.FILES['subject']
            correction = request.FILES['correction']
            categorie = form.cleaned_data['categorie']
            user=request.user
            
            data = Subject(subject=sujet, correction=correction, categorie=categorie, id_user=user)
            data.save()
    
            decompress_zip("./data/corrections/"+correction.name,"./data/corrections/")
            sans_zip = remove_zip_extension(correction.name)
            compile_and_execute_correction('./data/corrections/'+sans_zip+'/src',"/home/smakalou/INSA/Projet-application/app/blog/test/resultat.txt")
            return redirect('p_redirect')
        else:
            errors = form.errors
            print(errors)
            
    else:
        form = forms.SubmitSubject()
    return render(request, 'blog/p_submit.html',
                  context={'formu': form})
    
def submitWork(request):
    
    form = forms.SubmitWork(request.POST, request.FILES)
    if request.method =='POST':
        form = forms.SubmitWork(request.POST, request.FILES)
        
        if form.is_valid():

            categorie = form.cleaned_data['categorie']
            devoir = request.FILES['devoir']
            user=request.user
            data = Subject(categorie=categorie, devoir=devoir, id_user=user)
            data.save()
            return redirect('e_redirect')
    else:
        form = forms.SubmitWork()
    return render(request, 'blog/e_submit.html',
                  context={'formi': form})


def p_redirect(request):
    
    return render(request, 'blog/p_redirect.html')

def e_redirect(request):
    
    return render(request, 'blog/e_redirect.html')