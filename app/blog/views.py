from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . import forms, models
import authentication.models
from blog.models import *
from blog.test.compare import *
from blog.compilation import *
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from django.http import HttpResponse
from django.conf import settings



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

            # Vérifier si l'élève a déjà une note pour la catégorie donnée
            has_grade = Resultat.objects.filter(id_user=user, id_subject__categorie=categorie).exists()
            if has_grade:
                # Rediriger ou afficher un message d'erreur indiquant à l'élève qu'il ne peut pas soumettre un autre sujet
                return HttpResponse('Vous avez déjà une note pour cette catégorie. Vous ne pouvez pas soumettre un autre sujet.')
            
            #Subject.objects.filter(id_user=user, categorie=categorie).delete() #Suppression des anciennes soumissions dans la BDD
           
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
    results = Resultat.objects.select_related('id_subject').filter(id_user=user)
    
    return render(request, 'blog/notes.html', {'results': results})


def view_student_notes(request):
    students = authentication.models.User.objects.filter(role='STUDENT')
    results1 = Resultat.objects.select_related('id_user').filter(id_user__in=students)
    print("******************")
    print(results1)
    return render(request, 'blog/notes.html', {'results1': results1})

def view_statistics(request):
    # Récupérer les données de notes pour les catégories "SYSTEME" et "GENTOO"
    results = Resultat.objects.filter(id_subject__categorie=Subject.SYSTEME)
    notes = [result.note for result in results]
    
    
    results1 = Resultat.objects.filter(id_subject__categorie=Subject.GENTOO)
    notes1 = [result.note for result in results1]
    

    # Créer le histogramme pour les catégories "SYSTEME" et "GENTOO"
    histogram = go.Histogram(x=notes, name='SYSTEME', opacity=0.7, nbinsx=20)
    
    histogram1 = go.Histogram(x=notes1, name='GENTOO', opacity=0.7, nbinsx=20)
    

    # Personnaliser le layout des diagrammes
    
    #SYSTEME
    layout = go.Layout(
        title='Répartition des notes - SYSTEME',
        xaxis=dict(title='Notes', range=[0, 20], dtick=1),
        yaxis=dict(title='Nombre d\'élèves')
    )
    
    #GENTOO
    layout1 = go.Layout(
        title='Répartition des notes - GENTOO',
        xaxis=dict(title='Notes', range=[0, 20], dtick=1),
        yaxis=dict(title='Nombre d\'élèves')
    )
    

    # Créer les figures à partir du histogramme et du layout
    fig = go.Figure(data=[histogram], layout=layout)  #SYSTEME
    fig1 = go.Figure(data=[histogram1], layout=layout1) #GENTOO
    

    # Convertir les figures en JSON pour les afficher dans le template
    graph_json = fig.to_json()
    graph_json1 = fig1.to_json()


    context = {'graph0': graph_json, 'graph1': graph_json1}
    return render(request, 'blog/statistics.html', context)



def show_availables(request):
    objets = Subject.objects.exclude(subject__exact='')
    print("***************************")
    print(objets[0].url)
    context = {'objets': objets}
    return render(request, 'blog/availables.html', context)
