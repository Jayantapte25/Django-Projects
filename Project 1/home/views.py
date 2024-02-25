from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.contrib import messages
from home.models import contact

# Learned URL dispatching here
def index(request):
    context = {
        'variable1':"This is sent",
        'variable2':"This is sent"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("This is homepage")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is services page")

def submit_contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
        contact1 = contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact1.save() 

        messages.success(request, 'Your message has been sent')
 
    return render(request, 'contact.html')
    # return HttpResponse("This is contact page")
