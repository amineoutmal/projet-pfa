from django.shortcuts import render
from globals.models import *
from django.core.files.storage import *
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.
def home(request):
    return render(request, 'clients/index.html')

def creer_intervention(request):
    list_panne = Panne.objects.all()
    list_equipement = Equipement.objects.all()  
    if request.method=='POST':
        titre= request.POST.get('titre')
        panne= request.POST.get('panne')
        equipement= request.POST.get('equipement')
        image= request.FILES['image']
        description= request.POST.get('description')

        imagename = image.name
        saveimage= FileSystemStorage()
        saveimage.save(imagename,image)
        
        idpanne=Panne.objects.filter(libelle_panne=panne).values('id')[0]['id']
        idequip=Equipement.objects.filter(nom_equipement=equipement).values('id')[0]['id']
        if 'id_client' in request.session:
            get_idClient=request.session['id_client']
        insertintervention = Intervention(Titre_intervention=titre,type_panne=Panne.objects.get(id=idpanne),image=imagename,description=description,etat='0',clients=Client.objects.get(id=get_idClient))
        insertintervention.save()
        insertintervention.equipements.add(Equipement.objects.get(id=idequip))
        
               

    return render(request, 'clients/forms/creer-intervention.html',{"panne":list_panne,"equipement":list_equipement})



def mes_intervention(request):
        if 'id_client' in request.session:
            get_idClient=request.session['id_client']
            Interv_client = Intervention.objects.all().filter(clients=get_idClient)
            inte_id = Interv_client.values_list('id')
            
            alls = Intervention.equipements.through.objects.all()
            print(alls.get())
            context = {
                'intervention':Interv_client
                }

            return render(request, 'clients/mes-intervention.html',context)
            
    
        
