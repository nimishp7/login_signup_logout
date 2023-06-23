from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as authlogin,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

def login(request):
    if request.method  == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            authlogin(request,user)
            return redirect('home')
        else:
            return HttpResponse('name or password is incorrect')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        name =request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            return redirect('home')
        else:
            my_user = User.objects.create_user(name, email,password1)
            my_user.save()
            return redirect('login')
        print(name, email,password1) 
    return render(request, 'signup.html')


def LogoutPage(request):
    logout(request)
    return redirect('login') 
    