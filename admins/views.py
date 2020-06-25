from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from globals.models import *
from .forms import *
import tkinter
import sweetify
from django.contrib.sessions.models import Session
from .decorators import unauthenticated_admin
from xhtml2pdf import pisa
from io import BytesIO
from django.http import HttpResponse
from django.views import View
from django.template.loader import get_template
import csv




@unauthenticated_admin
def home(request):
    
    return render(request, 'admins/index.html')
@unauthenticated_admin
def dashboard(request):
    count_interv = Intervention.objects.count()
    count_tech = Technicien.objects.count()
    count_client = Client.objects.count()
    context={'intervcount':count_interv,'clients':count_tech,'technicien':count_tech}
    return render(request, 'admins/dashboard.html',context)
@unauthenticated_admin
def client(request):
    return render(request, 'admins/client.html')

def logout(request):
    del request.session['admin_id']
    del request.session['admin_nom']
    del request.session['admin_email']
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



#facturation
def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

#Opens up page as PDF
class facturer(View):
    def get(self, request, *args, **kwargs):
        intervention_concern = Intervention.objects.get(id=self.kwargs.get('pk'))
        intervention_concern.etat = 5
        intervention_concern.save()
        idclient=Intervention.objects.filter(id=self.kwargs.get('pk')).values('clients_id')[0]['clients_id']
        facture=Facturation(etat=0,clients=Client.objects.get(id=idclient),interventions=Intervention.objects.get(id=self.kwargs.get('pk')))
        facture.save()
        context={'interv':intervention_concern}
        pdf = render_to_pdf('admins/facture.html', context)
        
        return HttpResponse(pdf, content_type='application/pdf')
        
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('app/pdf_template.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response



@unauthenticated_admin
def profile(request):
    pk=request.session['admin_id']
    if request.method=='GET':
            admin=Admin.objects.get(id=pk)
            form = adminform(instance=admin)
            return render(request, 'admins/forms/profile.html',{'form':form})
        
    else: 
        if pk==0:
            form = adminform(request.POST)
        else:
            admin=Admin.objects.get(id=pk)
            form = adminform(request.POST,instance=admin)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return render(request, 'admins/forms/profile.html',{'form':form})

@unauthenticated_admin
def csv_technicien(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['nom', 'email', 'tel', 'login','password','types','specialité'])

    for technicien in Technicien.objects.all().values_list('nom', 'email', 'tel', 'login','password','types','specialité'):
        writer.writerow(technicien)

    response['Content-Disposition'] = 'attachment; filename="techniciens-list.csv"'

    return response

@unauthenticated_admin
def csv_client(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['nom', 'email', 'tel', 'login','password','matricule_id','adresse'])
    for client in Client.objects.all().values_list('nom', 'email', 'tel', 'login','password','matricule_id','adresse'):
        writer.writerow(client)

    response['Content-Disposition'] = 'attachment; filename="clients-list.csv"'

    return response


@unauthenticated_admin
def csv_stock(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['nom_equipement', 'qte_stock', 'prix_equipement'])

    for equipe in Equipement.objects.all().values_list('nom_equipement', 'qte_stock', 'prix_equipement'):
        writer.writerow(equipe)

    response['Content-Disposition'] = 'attachment; filename="stocks.csv"'

    return response


@unauthenticated_admin
def csv_intervention(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Titre_intervention', 'date_intervention', 'type_panne','description','clients','latitude','longtude','fulladresses','date_fin','durée_mission'])

    for interv in Intervention.objects.all().values_list('Titre_intervention', 'date_intervention', 'type_panne__libelle_panne','description','clients__nom','latitude','longtude','fulladresses','date_fin','durée_mission'):
        writer.writerow(interv)

    response['Content-Disposition'] = 'attachment; filename="interventions.csv"'

    return response