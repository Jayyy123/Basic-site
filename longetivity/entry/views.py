from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'entry/loginpage.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    page = 'register'
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)  
        if form.is_valid():
            a = form.save(commit=False)
            a.username = a.username.lower
            a.save()
            messages.success(
                request, 'Account has been successfully created')

            login(request, a)
            return redirect('home')
            
        else:
            messages.error(
                request, 'An error has occured while registering!')

    return render(request, 'entry/signup.html', {'page':page, 'form':form})

def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
                
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request,'username does not exist')
        
        user = authenticate(
            request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(
                request,"Username or Password is incorrect")

    return render(request, 'entry/signin.html')

def signout(request):
    logout(request)
    messages.success(
        request, "user was logged out successfully")
    return redirect('loginpage')


def profile(request):
    return render(request, 'entry/profile.html')
