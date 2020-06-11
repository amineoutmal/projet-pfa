from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.sessions.models import Session

def unauthenticated_technicien(view_fun):
    def wrapper_fun(request,*args,**kwargs):
        if not 'technicien_id' in request.session:
            return redirect('loginPage')
        else:
            return view_fun(request,*args,**kwargs)
    return wrapper_fun
