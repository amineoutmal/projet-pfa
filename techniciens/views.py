from django.shortcuts import render
from .decorators import unauthenticated_technicien
from globals.models import *
from django.shortcuts import redirect
from datetime import date
from datetime import datetime


# Create your views here.
@unauthenticated_technicien
def home(request):
    return render(request, 'techniciens/index.html')

def logout_technicien(request):
    del request.session['technicien_id']
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
            get_idTech=request.session['technicien_id']
            get_technicien=Technicien.objects.get(id=get_idTech)
            get_technicien.disponibilité=0
            get_technicien.save()
            get_interv = Intervention.objects.get(id=pk)
            date_debut = get_interv.date_intervention
            get_interv.etat = 3
            today = date.today()
            days = days_between(date_debut, today) * 24 
            get_interv.date_fin = today
            get_interv.durée_mission = days
            get_interv.save()
       
            return redirect('mes_interventions')