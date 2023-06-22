from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . import forms, models
from blog.models import *
from blog.test.compare import *
from blog.compilation import *
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import glob

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
            
            path= "./data/corrections/"+categorie_name+ "/" + sans_zip
            decompress_zip("./data/corrections/"+ correction.name, path)
            
            correction_txt = os.getcwd() + "/blog/test/resultat.txt"
            print(correction_txt)
           
            compile_and_execute_correction(path + '/src', correction_txt)
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

            print("******************************************")
            print(devoir.name)
            
            categorie_name = subject_instance.get_categorie_display()
            path_devoirs = "./data/devoirs/"+ categorie_name + "/" + sans_zip
            decompress_zip("./data/devoirs/"+ devoir.name, path_devoirs)
            
            devoir_txt = os.getcwd() + "/blog/test/resultat_etudiant.txt"
            correction_txt = os.getcwd() + "/blog/test/resultat.txt"
           
            note = compile_exec_text("./data/corrections/" + categorie_name + "/" + sans_zip +"/src/main.c"
                              ,path_devoirs +'/src', devoir_txt, correction_txt)

            # Iterate over the zip files and delete them
            for zip_file in glob.glob(os.path.join("./data/devoirs", '*.zip')):
                os.remove(zip_file)

            print("All zip files have been deleted.")

            
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
