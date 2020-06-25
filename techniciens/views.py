from django.shortcuts import render
from .decorators import unauthenticated_technicien
from globals.models import *
from django.shortcuts import redirect
from datetime import date
from datetime import datetime
from .forms import *



# Create your views here.
@unauthenticated_technicien
def home(request):
    return render(request, 'techniciens/index.html')

def logout_technicien(request):
    del request.session['technicien_id']
    del request.session['technicien_nom']
    del request.session['technicien_email']
    return redirect('loginPage')


#intervention _ Technicien
@unauthenticated_technicien
def mes_interventions(request):
            get_idTechnicien=request.session['technicien_id']
            Interv_ids = Affectation.objects.values('Inter').filter(tech=get_idTechnicien)
            inter = Intervention.objects.all().filter(id__in=Interv_ids)
            context = {
                'intervention':inter
                }
           
            #Intervention = Intervention.objects.get(id=)
            return render(request, 'techniciens/mes-intervention.html',context)


@unauthenticated_technicien
def track_interv_technicien(request,pk):
    if request.method=="GET":
        get_interv= Intervention.objects.get(id=pk)
        context = {
                    'inter':get_interv,
                    
                    } 
        return render(request, 'techniciens/track_intervention.html',context)


def days_between(d1, d2):
    return abs((d2 - d1).days)


@unauthenticated_technicien
def terminer(request,pk):
        get_interv= Intervention.objects.get(id=pk)
        if request.method=='POST':
            equipements = request.POST.getlist('equipements')
            qte = request.POST.get('qte')
            for equip in equipements:
                for qt in qte:
                    d=Detail_equipement(equipements=Equipement.objects.get(id=equip),interventions=Intervention.objects.get(id=pk),QTE=qt)
                    d.save()

        
        context = {
                    'interv':get_interv,
                    
                    }
        return render(request, 'techniciens/terminer_interv.html',context)
           


@unauthenticated_technicien
def profile(request):
    pk=request.session['technicien_id']
    if request.method=='GET':
            technicien=Technicien.objects.get(id=pk)
            form = technicienformprofile(instance=technicien)
            return render(request, 'techniciens/profile.html',{'form':form})
        
    else: 
        if pk==0:
            form = technicienformprofile(request.POST)
        else:
            technicien=Technicien.objects.get(id=pk)
            form = technicienformprofile(request.POST,instance=technicien)
        if form.is_valid():
            form.save()
            return redirect('acceuil-technicien')
    return render(request, 'techniciens/profile.html',{'form':form})