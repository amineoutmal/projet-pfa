from django.shortcuts import render,HttpResponse , redirect
from django.contrib.auth.decorators import login_required
from globals.models import *
from .forms import *
import tkinter
import sweetify

def home(request):
    return render(request, 'admins/index.html')
def dashboard(request):
    return render(request, 'admins/dashboard.html')
def client(request):
    return render(request, 'admins/client.html')

#intervention-operation

def intervention(request):
                if request.method == 'POST':
                    technicien_id = request.POST.get('technicienaffecter')
                    intervention_id = request.POST.get('intervconcerner')
                    affecter = Affectation(tech=Technicien.objects.get(id=technicien_id),Inter=Intervention.objects.get(id=intervention_id)).save()
                    get_interv = Intervention.objects.get(id=intervention_id)
                    get_interv.etat = 1
                    if get_interv.save():
                        get_Technicien = Technicien.objects.get(id=technicien_id)
                        get_Technicien.disponibilité = 1
                        get_Technicien.save()


                All_interv = Intervention.objects.all()
                Tech_list = Technicien.objects.filter(disponibilité="0").all()
                context = {
                    'All_intervention':All_interv,
                    'Tech_list':Tech_list
                    }      
                return render(request, 'admins/intervention.html',context)

def delete_interv_admin(request,pk):
            get_interv = Intervention.objects.get(id=pk)
            get_interv.delete()
       
            return redirect('intervention')
            


def stock(request):
    return render(request, 'admins/stock.html')

def ticket(request):
    return render(request, 'admins/ticket.html')

def technicien(request):
    
    return render(request, 'admins/technicien.html')

###crud client### 
  
def forms_client(request,pk=0):
    
    if request.method=='GET':
        if pk==0:   #check update or insert
            form = clientform()
        else:
            client=Client.objects.get(id=pk)
            form = clientform(instance=client)
        return render(request, 'admins/forms/form_client.html',{'form':form})
        
    else: 
        if pk==0:
            form = clientform(request.POST)
        else:
            client=Client.objects.get(id=pk)
            form = clientform(request.POST,instance=client)
        if form.is_valid():
            form.save()
            return redirect('client')
    return render(request, 'admins/forms/form_client.html',{'form':form})


def client(request):
    client = Client.objects.all()
    context= {'client':client}
    return render(request, 'admins/client.html',context)

def supp_clt(request,pk):
    client = Client.objects.get(id=pk)
    client.delete()    
    return redirect('client')

#crud equipement


def forms_equipement(request,pk=0):
    
    if request.method=='GET':
        if pk==0:   #check update or insert
            form = stockform()
        else:
            equipement=Equipement.objects.get(id=pk)
            form = stockform(instance=equipement)
        return render(request, 'admins/forms/form_stock.html',{'form':form})
        
    else: 
        if pk==0:
            form = stockform(request.POST)
        else:
            equipement=Equipement.objects.get(id=pk)
            form = stockform(request.POST,instance=equipement)
        if form.is_valid():
            form.save()
            return redirect('stock')
    return render(request, 'admins/forms/form_stock.html',{'form':form})


def supp_equip(request,pk):
    equipement = Equipement.objects.get(id=pk)
    equipement.delete()    
    return redirect('stock')


    
def stock(request):
    equipement = Equipement.objects.all()
    context= {'equipement':equipement}
    return render(request, 'admins/stock.html',context)

#crud technicien

def technicien(request):
    technicien=Technicien.objects.all()
    context= {'technicien':technicien}
    return render(request, 'admins/technicien.html',context)

def forms_technicien(request,pk=0):
    
    if request.method=='GET':
        if pk==0:   #check update or insert
            form = technicienform()
        else:
            technicien=Technicien.objects.get(id=pk)
            form = technicienform(instance=technicien)
                
        return render(request, 'admins/forms/form_technicien.html',{'form':form})
        
    else: 
        if pk==0:
            form = technicienform(request.POST)
        else:
            technicien=Technicien.objects.get(id=pk)
            form = technicienform(request.POST,instance=technicien)
        if form.is_valid():
            form.save()
            return redirect('technicien')
    return render(request, 'admins/forms/form_technicien.html',{'form':form})


def supp_tech(request,pk):
    technicien = Technicien.objects.get(id=pk)
    technicien.delete()    
    return redirect('technicien')

#crud panne #
def panne(request):
    panne = Panne.objects.all()
    contexte={'panne':panne}
    return render(request, 'admins/panne.html',contexte)
    
def forms_panne(request,pk=0):
    
    if request.method=='GET':
        if pk==0:   #check update or insert
            form = panneform()
        else:
            panne=Panne.objects.get(id=pk)
            form = panneform(instance=panne)
        return render(request, 'admins/forms/form_panne.html',{'form':form})
        
    else: 
        if pk==0:
            form = panneform(request.POST)
        else:
            panne=panneform.objects.get(id=pk)
            form = panneform(request.POST,instance=panne)
        if form.is_valid():
            form.save()
            return redirect('panne')
    return render(request, 'admins/forms/form_panne.html',{'form':form})
def supp_panne(request,pk):
    panne = Panne.objects.get(id=pk)
    panne.delete()    
    return redirect('panne')
    

