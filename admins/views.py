from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'admin/index.html')
def client(request):
    return render(request, 'admin/client.html')
def intervention(request):
    return render(request, 'admin/intervention.html')
def stock(request):
    return render(request, 'admin/stock.html')
def equipement(request):
    return render(request, 'admin/equipement.html')
def ticket(request):
    return render(request, 'admin/ticket.html')
def technicien(request):
    return render(request, 'admin/technicien.html')