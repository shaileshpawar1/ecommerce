from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .models import User
# Create your views here.

def login_view(request):
    
    if request.method == 'POST':
        # try :
        email = request.POST.get('email',None)   
        password = request.POST.get('password',None)
        (f'Login:\t{email}\nPassword:\t{password}')
        user =  User.objects.first()
        print(user.email)
        print(user.password)
        print(make_password(password))

        # user = authenticate(email=email, password=make_password(password))
        # if user is not None:
        #     redirect(profile_view)
        # else:
        #     return redirect(login_view)    
        # except:
        return redirect(login_view)

    if request.method == 'GET':
        return render( request,'login.html')

def logout_view(request):
    return render(request, 'logot.html' )

def profile_view(request):
    return render(request,'profile.html')
