from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

# returns HTTP response of Hello, World
def index(request):
    return HttpResponse("Hello, World!")

def index(request):
    return render(request, 'index.html')

def Asyikin(request):
    return HttpResponse("Hello, Asyikin")

def Guests(request):
    return HttpResponse("Hello, Guests")

# we can use any Python logic inside our greet function
# capitalize = capitalizes teh first letter of string 
def greet(request, name):
    return HttpResponse(f'Hello, {name.capitalize()}')