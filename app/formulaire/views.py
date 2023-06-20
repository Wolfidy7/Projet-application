from django.http import HttpResponse
from django.shortcuts import redirect, render
from formulaire.models import Data
from formulaire.forms import SendWork
from .compilation import *
from tests.result import compare
from time import *
import shutil

def hello(request):
    
    datas = Data.objects.all()
    return render(request, 'formulaire/hello.html',
                  {'first':datas[0]})
    

def submit(request):
    
    
    if request.method =='POST':
        form = SendWork(request.POST, request.FILES) #ajout du formulaire
        
        if form.is_valid():
            
            fichier = request.FILES['file']
            nom = request.POST.get('name')
            print(fichier)
            print(nom)
            
            # Enregistrer le nom du fichier et le fichier dans la base de données
            data = Data(name=nom, file= fichier)
            data.save()
            sleep(1)
            #récupétation de tous les fichiers so
            student_dir = "tests/sample_etudiant/" + nom
            correction_main = "/home/dini/Projet-application/app/tests/sample_correction/src/main.c"
            decompress_zip(fichier, student_dir)

            # copy main file
            shutil.copy(correction_main, student_dir  + "/TP_miniglibc/src")
        
            # test de chaque fichier
            compare.compile_exec_text( student_dir  + "/TP_miniglibc/src")
            return redirect('redirection')
    
    else:
        form = SendWork()
        
    return render(request,
                  'formulaire/submit.html',
                  {'formulaire': form}) #passe le formulaire au gabarit
    
    
    
    
'''def receive_form(request):
    if request.method == 'POST':
        nom = request.POST.get('name')
        fichier = request.FILES.get('file')
        
    return render(request, 'formulaire/cible.html')'''
        

def redirect_view(request):
    
    return render(request, 'formulaire/redirect.html')
    

