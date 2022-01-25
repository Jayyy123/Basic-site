from django.shortcuts import redirect, render
from .models import Details
from .forms import HeartForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'heart/home.html')

# @login_required(login_url="loginpage")
def form(request):
    a = HeartForm()
    if request.method == 'POST':
        a = HeartForm(request.POST,request.FILES)
        if a.is_valid():
            a.save()
        return redirect('database')
    return render(request, 'heart/form.html', {'a':a})

def database(request):
    a = Details.objects.all
    return render(request, 'heart/database.html', {'a':a})

def editbase(request, pk):
    a = Details.objects.get(id =pk)
    b = HeartForm(instance=a)
    if request.method == 'POST':
        b = HeartForm(request.POST, request.FILES,instance=a)
        if b.is_valid():
            b.save()
        return redirect('database')
    return render(request, 'heart/form.html', {'a':b})

def deletebase(request, pk):
    a = Details.objects.get(id=pk)
    if request.method == 'POST':
        a.delete()
        return redirect('database')
    return render(request, 'heart/deletebase.html', {'a':a})

def result(request):
    return render(request, 'heart/result.html')


def multi(request, pk):
    a = Details.objects.get(id = pk)
    return render(request, 'heart/multi.html', {'a':a})