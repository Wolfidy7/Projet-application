from django.http import HttpResponse
from django.shortcuts import redirect, render
from formulaire.models import Data
from formulaire.forms import SendWork
from formulaire.compilation import process_zip 
def hello(request):
    
    datas = Data.objects.all()
    return render(request, 'formulaire/hello.html',
                  {'first':datas[0]})
    


def submit(request):
    if request.method == 'POST':
        form = SendWork(request.POST, request.FILES)

        if form.is_valid():
            fichier = request.FILES['file']
            nom = request.POST.get('name')
            print(fichier)
            print(nom)

            # Enregistrer le nom du fichier et le fichier dans la base de données
            data = Data(name=nom, file=fichier)
            data.save()

            # Décompresser et compiler les fichiers
            destination_directory = 'Projet-application/app/files'
            process_zip(fichier, destination_directory)

            return redirect('redirection')

    else:
        form = SendWork()

    return render(request, 'formulaire/submit.html', {'formulaire': form})

    
    
    
'''def receive_form(request):
    if request.method == 'POST':
        nom = request.POST.get('name')
        fichier = request.FILES.get('file')
        
    return render(request, 'formulaire/cible.html')'''
        

def redirect_view(request):
    
    return render(request, 'formulaire/redirect.html')
    

