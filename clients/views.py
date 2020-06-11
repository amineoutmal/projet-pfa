from django.shortcuts import render
from globals.models import *
from django.core.files.storage import *
from django.contrib import messages
from django.shortcuts import redirect
from .decorators import unauthenticated_client


# Create your views here.
def logout_client(request):
    del request.session['id_client']
    return redirect('loginPage')
@unauthenticated_client
def home(request):
    return render(request, 'clients/index.html')
@unauthenticated_client
def creer_intervention(request):
    list_panne = Panne.objects.all()
    list_equipement = Equipement.objects.all()  
    if request.method=='POST':
        titre= request.POST.get('titre')
        panne= request.POST.get('panne')
        equipementss= request.POST.getlist('equipement')
        image= request.FILES['image']
        description= request.POST.get('description')
        longitudes= request.POST.get('loc_long')
        latitudes= request.POST.get('loc_lat')
        fulladresse= request.POST.get('search_input')
        

        imagename = titre+image.name
        saveimage= FileSystemStorage()
        saveimage.save(imagename,image)
        
        idpanne=Panne.objects.filter(libelle_panne=panne).values('id')[0]['id']
        #idequip=Equipement.objects.filter(nom_equipement=equipement).values('id')[0]['id']
        if 'id_client' in request.session:
            get_idClient=request.session['id_client']
        insertintervention = Intervention(Titre_intervention=titre,type_panne=Panne.objects.get(id=idpanne),image=imagename,description=description,etat='0',clients=Client.objects.get(id=get_idClient),latitude=latitudes,longtude=longitudes,fulladresses=fulladresse)
        insertintervention.save()
        for eq in equipementss:
            insertintervention.equipements.add(Equipement.objects.get(id=eq))
            return redirect('mes-intervention')
            
        
        
                
       
        
               

    return render(request, 'clients/forms/creer-intervention.html',{"panne":list_panne,"equipement":list_equipement})


@unauthenticated_client
def mes_intervention(request):
            get_idClient=request.session['id_client']
            Interv_client = Intervention.objects.all().filter(clients=get_idClient)

            context = {
                'intervention':Interv_client
                }

            return render(request, 'clients/mes-intervention.html',context)
            
    
@unauthenticated_client        
def validate_interv(request,pk):

            get_interv = Intervention.objects.get(id=pk)
            get_interv.etat = 1
            get_interv.save()
       
            return redirect('mes-intervention')
@unauthenticated_client
def delete_interv(request,pk):

            get_interv = Intervention.objects.get(id=pk)
            get_interv.delete()
       
            return redirect('mes-intervention')
            
    