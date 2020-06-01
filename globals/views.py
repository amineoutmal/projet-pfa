from django.shortcuts import render
from validate_email import validate_email
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from .models import *
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
import json
from admins import views
from django.contrib import messages
from django.views import View
import random
from django.core.mail import EmailMessage
from django.contrib.sessions.models import Session




# Login INSTRUCTIONS

def checkclient(login,password):
    num_results = Client.objects.filter(login = login , password = password).count()
    if num_results > 0 :
        return 'true'
    else:
        return 'false'
    

def checktechnicien(login,password):
    num_results = Technicien.objects.filter(login = login , password = password).count()
    if num_results > 0 :
        return 'true'
    else:
        return 'false'

def checkadmin(login,password):
    num_results = Admin.objects.filter(login = login , password = password).count()
    if num_results > 0 :
        return 'true'
    else:
        return 'false'

def loginPage(request):
    if request.method=='POST':
        logins= request.POST.get('username')
        passwords= request.POST.get('password')
        if checkclient(logins,passwords)=="true":
            request.session['id_client']= Client.objects.filter(login=logins).values('id')[0]['id']
            return redirect('acceuil')
        elif checktechnicien(logins,passwords)=="true":
            request.sessions['technicien_id'] = Technicien.objects.filter(login=logins).values('id')[0]['id']
            return HttpResponse(id)
        elif checkadmin(logins,passwords)=="true":
            return redirect('home')
        else :
            messages.info(request,'Mot De Passe Ou User Incorrect')


    return render(request, 'registration/login.html')







# Register INSTRUCTIONS

def checkclientemail(email):
    client = Client.objects.all()
    for cl in client:
        if cl.email == email:
            return 'true'
        else:
            return 'false'

class EmailValidationView(View):
    def post(self,request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error':'Email n est pas valide'})
        if checkclientemail(email)=="true":
            return JsonResponse({'email_error':'Email Déja Utiliser'})
        return JsonResponse({'email_valid':True})

def registerPage(request):
    if request.method=='POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        email = request.POST['email']
        telephone = request.POST['telephone']
        password = request.POST['password']
        password2 = request.POST['secondpassword']
        login = request.POST['Username']
        matricule_id= random.randrange(25, 250, 5)
        ville = request.POST['ville']
        zips = request.POST['zip']
        adresses = request.POST['adresse']
        fulladresse = ville +''+zips +''+ adresses
        
        if(password == password2):
            insertclient = Client(nom=nom,email=email,tel=telephone,login=login,password=password,matricule_id=matricule_id,adresse=fulladresse).save()
            
            return redirect('loginPage')
        else:
             messages.info(request,'Les Deux Mot De Passe Sont Pas Les Memes')
            

        
    
    return render(request, 'registration/register.html')
