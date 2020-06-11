from django.shortcuts import render,HttpResponse , redirect
from django.contrib.auth.decorators import login_required
from globals.models import *
from .forms import *
import tkinter
import sweetify
from django.contrib.sessions.models import Session
from .decorators import unauthenticated_admin

@unauthenticated_admin
def home(request):
    return render(request, 'admins/index.html')
@unauthenticated_admin
def dashboard(request):
    return render(request, 'admins/dashboard.html')
@unauthenticated_admin
def client(request):
    return render(request, 'admins/client.html')

def logout(request):
    del request.session['admin_id']
    return redirect('loginPage')











#intervention-operation
@unauthenticated_admin
def intervention(request):
                if request.method == 'POST':
                    technicien_id = request.POST.get('technicienaffecter')
                    intervention_id = request.POST.get('intervconcerner')
                    affecter = Affectation(tech=Technicien.objects.get(id=technicien_id),Inter=Intervention.objects.get(id=intervention_id)).save()
                    get_interv = Intervention.objects.get(id=intervention_id)
                    get_interv.etat = 2
                    if get_interv.save():
                        get_Technicien = Technicien.objects.get(id=technicien_id)
                        get_Technicien.disponibilité = 1
                        if get_Technicien.save():
                             sweetify.info(self.request, 'Message sent', button='Ok', timer=3000)

                All_interv = Intervention.objects.all()
                Tech_list = Technicien.objects.filter(disponibilité="0").all()
                context = {
                    'All_intervention':All_interv,
                    'Tech_list':Tech_list
                    }      
                return render(request, 'admins/intervention.html',context)
   
@unauthenticated_admin
def delete_interv_admin(request,pk):
            get_interv = Intervention.objects.get(id=pk)
            get_interv.delete()
       
            return redirect('intervention')
            

@unauthenticated_admin
def stock(request):
    return render(request, 'admins/stock.html')
@unauthenticated_admin
def ticket(request):
    return render(request, 'admins/ticket.html')
@unauthenticated_admin
def technicien(request):
    
    return render(request, 'admins/technicien.html')

@unauthenticated_admin
def track_interv(request,pk):
    if request.method=="GET":
        get_interv= Intervention.objects.get(id=pk)
        context = {
                    'inter':get_interv,
                    
                    } 
        return render(request, 'admins/track_intervention.html',context)








###crud client### 
@unauthenticated_admin
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

@unauthenticated_admin
def client(request):
    client = Client.objects.all()
    context= {'client':client}
    return render(request, 'admins/client.html',context)

@unauthenticated_admin
def supp_clt(request,pk):
    client = Client.objects.get(id=pk)
    client.delete()    
    return redirect('client')

#crud equipement

@unauthenticated_admin
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

@unauthenticated_admin
def supp_equip(request,pk):
    equipement = Equipement.objects.get(id=pk)
    equipement.delete()    
    return redirect('stock')


@unauthenticated_admin   
def stock(request):
    equipement = Equipement.objects.all()
    context= {'equipement':equipement}
    return render(request, 'admins/stock.html',context)

#crud technicien
@unauthenticated_admin
def technicien(request):
    technicien=Technicien.objects.all()
    context= {'technicien':technicien}
    return render(request, 'admins/technicien.html',context)
@unauthenticated_admin
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

@unauthenticated_admin
def supp_tech(request,pk):
    technicien = Technicien.objects.get(id=pk)
    technicien.delete()    
    return redirect('technicien')

#crud panne #
@unauthenticated_admin
def panne(request):
    panne = Panne.objects.all()
    contexte={'panne':panne}
    return render(request, 'admins/panne.html',contexte)
@unauthenticated_admin   
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
@unauthenticated_admin
def supp_panne(request,pk):
    panne = Panne.objects.get(id=pk)
    panne.delete()    
    return redirect('panne')
    

