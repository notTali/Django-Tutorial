from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse


def home(request):
    return render(request, 'home.html') # HttpResponse('Home Page')

def room(request):
    return render(request, 'room.html') #HttpResponse('Room')