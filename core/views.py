from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from .models import Warehouse, Vehicle, VEHICLE_GOOD_LIST, WAREHOUSE_GOOD_LIST, Notification
from django.http import HttpResponse
from django.contrib.sessions.middleware import SessionMiddleware
from django import forms
from django.shortcuts import render
from django.contrib.auth.decorators import login_required




# Create your views here.
isSegmented = False

@login_required(login_url="logIn")
def home(request):
    currentUser = request.user
    warehouses = Warehouse.objects.filter(user = currentUser)
    vehicles = Vehicle.objects.filter(user = currentUser)
    notifs = Notification.objects.filter(user = currentUser)
    
    return render(request, "home.html", {'currentUser' : currentUser, 'warehouses':warehouses, 'vehicles':vehicles, 'vehicleGoodList': VEHICLE_GOOD_LIST, 'warehouseGoodList':WAREHOUSE_GOOD_LIST, 'notifs':notifs})

def logOut(request):
    logout(request)
    return redirect('logIn')
    
    
def logIn(request):
    message1 = ""
    
    if request.method == 'POST':
        usernameUp = request.POST.get('usernameUp')
        emailUp = request.POST.get('emailUp')
        passwordUp = request.POST.get("passwordUp")
        usernameIn = request.POST.get('usernameIn')
        passwordIn = request.POST.get('passwordIn')
        
        if(usernameUp != None and emailUp != None and passwordUp != None):
            if User.objects.filter(email = emailUp).exists() or User.objects.filter(username = usernameUp).exists():
                pass
            else:
                user = User.objects.create_user(username=usernameUp, password=passwordUp)
                
                user.save()
        elif(usernameIn != None and passwordIn != None):
             
             user = auth.authenticate(username=usernameIn, password=passwordIn)
             if user != None:
                auth.login(request,user)
                message1 = "Success"
                return redirect('home')
             else:
                message1 = "Invalid Credential"
                
                return render (request,"logIn.html",{"error" : message1}) 
        
    
    return render (request,"logIn.html",{"error" : message1})


  

def checkStatus(request):
    
    
    return redirect('home')


   