
from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages



# Create your views here.


def index(reruest):

    context={
        'variable':"this  is variable"
    }
    return render(reruest,'index.html',context)

def about(reruest):
    return render(reruest,'about.html')


def contact(request):
    if request.method=="POST":
        name=request.POST.get("name"),
        email=request.POST.get("email"),
        contact=request.POST.get("contact"),
        desc=request.POST.get("desc"),

        contact=Contact(name=name,email=email,contact=contact,desc=desc,datetime=datetime.today())
        contact.save()

        messages.success(request, 'Your message has been sent....')

    return render(request,'contact.html')

def services(request):
    return HttpResponse("This is services page")

def pricing(request):
    return render(request,'pricing.html')

def hotels(request):
    return render(request,'hotels.html')
