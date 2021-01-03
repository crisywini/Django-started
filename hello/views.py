from django.shortcuts import render
from django.http import HttpResponse #Import the HttpResponse function
# Create your views here.

def myView(request):
    return HttpResponse('Hello World! <br> Hola')
