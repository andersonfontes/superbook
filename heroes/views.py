from django.shortcuts import render
from django.http import HttpResponse

def hello_heroes(request):
    return HttpResponse("Bem-vindo ao módulo Heroes!")

# Create your views here.
