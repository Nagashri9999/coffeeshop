from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.views import generic

from django.core.mail import send_mail
from django.conf import settings
from django.core import mail
from django.core.mail.message import EmailMessage

# Create your views here.
def index(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html') 

def gallery(request):
    return render(request,'gallery.html')
def handlesignup(request):
    if request.method == "POST":
        uname=request.POST.get("username")
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        pass1=request.POST.get("pass1")
        pass2=request.POST.get("pass2")
        if pass1!=pass2:
            messages.error(request,"Password Do not Match")
        
        try:
            if User.objects.get(username=uname):
                messages.warning(request,"Username is Taken")
                return redirect('/signup')
        except Exception as identifier:
            pass
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return redirect('/signup')
        except Exception as identifier:
            pass
        myuser=User.objects.create_user(uname,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Signup Successful! Please Login Now")
        return redirect('/login')
       
    return render(request,'signup.html')

def handlelogin(request):

    if request.method == "POST":
        uname=request.POST.get("username")
        pass1=request.POST.get("pass1")
        myuser=authenticate(username=uname,password=pass1)

        if myuser is not None:
            login(request,myuser)
            messages.info(request,"Login Success")
            return redirect('/order')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')

    return render(request,'login.html')

def handlelogout(request):
    logout(request)
    messages.success(request,"Logout Successful")
    return redirect('/login')

def order(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    else:
        return render(request,'order.html')
    
	

def orderplaced(request) :
    return render(request,'orderplaced.html')     




   




   