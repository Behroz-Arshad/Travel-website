from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages




# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,"Wrong Credential")
            return redirect('/')

    else:
        return render(request,'accounts/login.html')

def register(request):
    if request.method == 'POST':
        first_name= request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_name=request.POST.get('username')
        password1 = request.POST.get('password1')
        password2=request.POST.get('password2')
        email = request.POST.get('email')

        if password1== password2:
            if(User.objects.filter(username=user_name).exists()):
                messages.info(request,"user name is already taken")
                print("user name is already taken")
            elif(User.objects.filter(email=email).exists()):
                messages.info(request, "email is already taken")
                print("email is already taken")
            else:
                user=User.objects.create_user(first_name=first_name,username=user_name,last_name=last_name,password=password1,email=email)
                user.save()
                print("created")
                return render(request, 'accounts/login.html')
        else:
            messages.info(request, "password not matched")
            print("password not matched")
            return render(request, 'accounts/register.html')
        return render(request, 'accounts/register.html')


    else:
        return render(request, 'accounts/register.html')
