from django.shortcuts import render
from globals.models import *
from django.core.files.storage import *
from django.contrib import messages
from django.shortcuts import redirect
from .decorators import unauthenticated_client
from .forms import *
import csv
from django.http import HttpResponse



# Create your views here.
def logout_client(request):
    del request.session['id_client']
    del request.session['client_nom']
    del request.session['client_email']
    
    return redirect('loginPage')

@unauthenticated_client
def home(request):
    id_client=request.session['id_client']
    count_interv = Intervention.objects.filter(clients=Client.objects.get(id=id_client)).count()
    FacturePayé = Intervention.objects.filter(clients=Client.objects.get(id=id_client),etat=6).count()
    FactureNonPayé = Intervention.objects.filter(clients=Client.objects.get(id=id_client),etat=5).count()
    context={'intervcount':count_interv,'FactureNonPayé':FactureNonPayé,'FacturePayé':FacturePayé}
    return render(request, 'clients/index.html',context)

@unauthenticated_client
def creer_intervention(request):
    list_panne = Panne.objects.all()
    list_equipement = Equipement.objects.all()  

    if request.method=='POST':
        titre= request.POST.get('titre')
        panne= request.POST.get('panne')
        equipementss= request.POST.getlist('equipements')
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
        get_idClient=request.session['id_client']
        insertintervention = Intervention(Titre_intervention=titre,type_panne=Panne.objects.get(id=idpanne),image=imagename,description=description,etat='0',clients=Client.objects.get(id=get_idClient),latitude=latitudes,longtude=longitudes,fulladresses=fulladresse)
        insertintervention.save()
        insertintervention.equipements.add(*equipementss)
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


def mes_facture(request):
        get_idClient=request.session['id_client']
        Interv_client = Intervention.objects.all().filter(clients=get_idClient,etat=5)

        context = {
                'intervention':Interv_client
                }
        return render(request, 'clients/mes-facture.html',context)

    
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

@unauthenticated_client
def valider_intervention(request,pk):
        intervention_concern = Intervention.objects.get(id=pk)
        intervention_concern.etat = 4
        intervention_concern.save()

        return redirect('mes-intervention')
            


@unauthenticated_client
def profile(request):
    pk=request.session['id_client']
    if request.method=='GET':
            client=Client.objects.get(id=pk)
            form = clientformprofile(instance=client)
            return render(request, 'clients/forms/profile.html',{'form':form})
        
    else: 
        if pk==0:
            form = clientformprofile(request.POST)
        else:
            client=Client.objects.get(id=pk)
            form = clientformprofile(request.POST,instance=client)
        if form.is_valid():
            form.save()
            return redirect('acceuil')
    return render(request, 'clients/forms/profile.html',{'form':form})

@unauthenticated_client
def csv_client(request):
    pk=request.session['id_client']
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Titre_intervention', 'date_intervention', 'type_panne', 'etat','description','equipements'])

    for interv in Intervention.objects.all().filter(clients=Client.objects.get(id=pk)).values_list('Titre_intervention', 'date_intervention', 'type_panne__libelle_panne', 'etat','description','equipements__nom_equipement'):
        writer.writerow(interv)

    response['Content-Disposition'] = 'attachment; filename="intervention-client.csv"'

    return response


