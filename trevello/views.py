from django.shortcuts import render
from .models import Destination,Subscribe,Contacts
from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required
def index(request):
    dest=Destination.objects.all()

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        sub=Subscribe(name=name,email=email)

        sub.save()
    else:
        return render(request, 'trevello/index.html', {"dests": dest})
    return render(request,'trevello/index.html',{"dests":dest})

@login_required
def contact(request):
    if request.method=="POST":
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        print(email,subject,message)
        con=Contacts(email=email,subject=subject,message=message)
        con.save()
        return render(request,'trevello/contact.html')

    return render(request,'trevello/contact.html')