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
    if request.method == 'POST':
        form = forms.SubmitSubject(request.POST, request.FILES)
        if form.is_valid():
            sujet = request.FILES['subject']
            correction = request.FILES['correction']
            categorie = form.cleaned_data['categorie']
            user = request.user

            subject_instance = Subject(
                subject=sujet,
                correction=correction,
                categorie=categorie,
                id_user=user
            )
            subject_instance.save()

            categorie_name = subject_instance.get_categorie_display()
            sans_zip = remove_zip_extension(correction.name)
            # Utilisez la variable 'categorie_name' comme nécessaire
    
            decompress_zip("./data/corrections/"+ correction.name, "./data/corrections/"+categorie_name+ "/" + sans_zip +"/")
            print("************************************************************************************************************************")
            path= "./data/corrections/"+categorie_name+ "/" + sans_zip +"/"
            print(path)
            
           
            compile_and_execute_correction(path + '/src', "/home/smakalou/INSA/Projet-application/app/blog/test/resultat.txt")
            return redirect('p_redirect')
        else:
            errors = form.errors
            print(errors)
    else:
        form = forms.SubmitSubject()
    return render(request, 'blog/p_submit.html', context={'formu': form})

    
def submitWork(request):
    
    form = forms.SubmitWork(request.POST, request.FILES)
    if request.method =='POST':
        form = forms.SubmitWork(request.POST, request.FILES)
        
        if form.is_valid():

            categorie = form.cleaned_data['categorie']
            devoir = request.FILES['devoir']
            user=request.user
           
            subject_instance = Subject(
                categorie=categorie,
                devoir=devoir,
                id_user=user,
            )
         
            subject_instance.save() #Sauvegarde dans la table Subject de la BDD
            
            
            sans_zip = remove_zip_extension(devoir.name)
            categorie_name = subject_instance.get_categorie_display()
            decompress_zip("./data/devoirs/"+ devoir.name, "./data/devoirs/"+categorie_name+ "/" + sans_zip +"/")
            path= "./data/devoirs/"+categorie_name+ "/" + sans_zip +"/"
           
            note = compile_exec_text("./data/corrections/"+categorie_name+ "/" + sans_zip +"/src/main.c"
                              ,path+'/src',"/home/smakalou/INSA/Projet-application/app/blog/test/resultat_etudiant.txt","/home/smakalou/INSA/Projet-application/app/blog/test/resultat.txt")
            
            #Ajout des résultats de l'élève dans la table Resultat
            work_result=Resultat(
                id_user =user,
                id_subject = subject_instance,
                note=note,
            )
            work_result.save() #Sauvegarde dans la table Resultat de La BDD
            
            
            return redirect('e_submit')
    else:
        form = forms.SubmitWork()
    return render(request, 'blog/e_submit.html',
                  context={'formi': form})


def p_redirect(request):
    
    return render(request, 'blog/p_redirect.html')

def e_redirect(request):
    
    return render(request, 'blog/e_redirect.html')


def view_notes(request):
    user = request.user
    results = Resultat.objects.filter(id_user=user).select_related('id_subject')
    return render(request, 'blog/notes.html', {'results': results})

