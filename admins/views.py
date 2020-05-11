from django.shortcuts import render
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
def technicien(request):
    technicien = Technicien.objects.all()
    context= {'technicien':technicien}
    return render(request, 'admins/technicien.html',context)