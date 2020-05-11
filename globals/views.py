from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from admins import views
from django.contrib import messages

# Create your views here.

def checkclient(login,password):
    client = Client.objects.all()
    for cl in client:
        if cl.login == login and cl.password == password:
            return 'true'
        else:
            return 'false'

def checktechnicien(login,password):
    technicien = Technicien.objects.all()
    for tc in technicien:
        if tc.login == login and tc.password == password:
            return "true"
        else:
            return "false"

def checkadmin(login,password):
    admin = Admin.objects.all()
    for ad in admin:
        if ad.login == login and ad.password == password:
            return "true"
        else:
            return "false"

def loginPage(request):
    if request.method=='POST':
        logins= request.POST.get('username')
        passwords= request.POST.get('password')
        if checkclient(logins,passwords)=="true":
            return HttpResponse('je suis un client')
        elif checktechnicien(logins,passwords)=="true":
            return HttpResponse('je suis un technicien')
        elif checkadmin(logins,passwords)=="true":
            return redirect('home')
        else :
            messages.info(request,'Mot De Passe Ou User Incorrect')


    return render(request, 'registration/login.html')


def registerPage(request):
    return render(request, 'registration/register.html')

