from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader

def acc(request):
    return render(request,'acceuil.html')
