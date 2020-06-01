from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'clients/index.html')

def creer_intervention(request):
    return render(request, 'clients/forms/creer-intervention.html')
