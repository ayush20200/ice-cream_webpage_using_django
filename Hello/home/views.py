from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contacts as ContactModel

# Create your views here.
def index(request): 
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is aboutpage")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is servicespage")

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contacts = ContactModel(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contacts.save()

    return render(request,'contacts.html')
    #return HttpResponse("this is contacts page")
