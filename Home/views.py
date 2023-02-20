from django.shortcuts import render,redirect
from products.models import Products
from .forms import UserAddForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User, Group
from .decorators import admin_only

@admin_only
def Index(request):
    products = Products.objects.all()
    context = {
        "products":products
    }
    return render(request,"index.html",context)

def SignIn(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['pswd']
        user1 = authenticate(request, username = username , password = password)
        
        if user1 is not None:
            
            request.session['username'] = username
            request.session['password'] = password
            login(request, user1)
            return redirect('Index')
        
        else:
            messages.info(request,'Username or Password Incorrect')
            return redirect('SignIn')
    return render(request,"login.html")

def SignUp(request):
    form = UserAddForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get("email")
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Exists")
                return redirect('SignUp')
            if User.objects.filter(email = email).exists():
                messages.info(request,"Email Exists")
                return redirect('SignUp')
            else:
                new_user = form.save()
                new_user.save()
                
                group = Group.objects.get(name='user')
                new_user.groups.add(group) 
                
                messages.success(request,"User Created")
                return redirect('AdminHome')
            
    return render(request,"register.html",{"form":form})

def SignUpStaff(request):
    form = UserAddForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get("email")
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Exists")
                return redirect('SignUp')
            if User.objects.filter(email = email).exists():
                messages.info(request,"Email Exists")
                return redirect('SignUp')
            else:
                new_user = form.save()
                new_user.save()
                
                group = Group.objects.get(name='staff')
                new_user.groups.add(group) 
                messages.success(request,"User Created")
                return redirect('AdminHome')
            
    return render(request,"Stock/register.html",{"form":form})

def SignOut(request):
    logout(request)
    return redirect('Index')

