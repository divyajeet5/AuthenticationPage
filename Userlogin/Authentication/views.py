from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt

def home(request):
    return render(request, 'Authentication/index.html')



def Signup(request):

    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        lname = request.POST['lname']
        email = request.POST['email']
        passs = request.POST['passs']
        passwordd = request.POST['passwordd']

        if User.objects.filter(username=username):
            messages.error(request, "User name already exists")
            return redirect('signup')

        if User.objects.filter(email=email):
            messages.error(request, "E-mail is already registered")
            return redirect('signup')

        if passs != passwordd:
            messages.error(request, "Please check your password for mismatch")
            return redirect('signup')

        if not username.isalnum():
            messages.error(request, "Username should be Alpha-Numeric")
            return redirect('signup')



        myuser = User.objects.create_user(username, email, passs)
        myuser.first_name = name
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "User registered successfully")
        return redirect('signin')


    return render(request, 'Authentication/signup.html')



def Signin(request):

    if request.method == "POST":
        username = request.POST['username']
        passs = request.POST['passs']
        user = authenticate(username=username, password=passs)

        if user is not None:
            login(request, user)
            name = user.first_name
            return render(request, "Authentication/index.html", {'name': name})

        else:
            messages.error(request, "Credentials do not match")
            return redirect('signin')

    return render(request, 'Authentication/signin.html')






def Signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')



