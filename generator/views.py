from django.shortcuts import render
from django.http import HttpResponse
import random 


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwyz')

    if request.GET.get("uppercase"):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWYZ'))
    
    if request.GET.get("numbers"):
        characters.extend(list('1234567890'))
    
    if request.GET.get("special"):
        characters.extend(list("!@#$%^&*()"))

    length = int(request.GET.get("length"))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    
    return render(request, 'generator/password.html', {'password' : thepassword})



def about(request):
    return render(request, 'generator/about.html')

