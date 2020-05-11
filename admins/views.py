from django.shortcuts import render,HttpResponse , redirect
from django.contrib.auth.decorators import login_required
from globals.models import *

def home(request):
    return render(request, 'admins/index.html')
def client(request):
    return render(request, 'admins/client.html')
def intervention(request):
    return render(request, 'admins/intervention.html')
def stock(request):
    return render(request, 'admins/stock.html')
def equipement(request):
    return render(request, 'admins/equipement.html')
def ticket(request):
    return render(request, 'admins/ticket.html')
def supp_tech(request,pk):
    technicien = Technicien.objects.get(id=pk)
    technicien.delete()
    
    return redirect('technicien')

def modifer_tech(request):

     return render(request, 'admins/modifier_tech.html')
    
def technicien(request):
    technicien = Technicien.objects.all()
    context= {'technicien':technicien}
    return render(request, 'admins/technicien.html',context)