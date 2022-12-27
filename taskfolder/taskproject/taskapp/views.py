from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Hello Home")
def about(request):
    return render(request,"about.html")
def contact(request):
    return HttpResponse("CONTACT")
def details(request):
    return render(request,"details.html")
def thanks(request):
    return HttpResponse("Thanks")