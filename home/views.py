from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse ("this is the Home page")

def about(request):
    return HttpResponse ("this is the About page")

def contact(request):
    return HttpResponse ("this is the Contat page")

def projects(request):
    return HttpResponse ("this is the Projects page")
