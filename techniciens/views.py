from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'techniciens/index.html')

"""def creer_intervention(request):
    return render(request, 'techniciens/forms/creer-intervention.html')"""
