from django.http import HttpResponse
from django.shortcuts import render
from formulaire.models import Data
from formulaire.forms import SendWork
def hello(request):
    
    datas = Data.objects.all()
    return render(request, 'formulaire/hello.html',
                  {'first':datas[0]})
    

def submit(request):
    
    
    if request.method =='POST':
        form = SendWork(request.POST) #ajout du formulaire
        
        if form.is_valid():
            return redirect('data_sent_page')
    
    else:
        form = SendWork()
        
        
    return render(request,
                  'formulaire/submit.html',
                  {'formulaire': form}) #passe le formualire au gabarit
    

