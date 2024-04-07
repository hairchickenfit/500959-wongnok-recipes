from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from . import models as base_models


def home(request):
    context = {}
    return render(request, 'base/home.html', context)

def login_base(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'base/login.html', context)
    elif request.method == 'POST':
        email = request.POST.get('floatingInput', None)
        password = request.POST.get('floatingPassword', None)
        try:
            if (email != None) and (password != None):
                wongnok_user_obj = authenticate(request, email=email, password=password)
                if wongnok_user_obj != None:
                    login(request, wongnok_user_obj)
                    return redirect('home')
                else:
                    messages.error(request, 'provided email and password cannot be authenticated')
            else:
                messages.error(request, 'email or/and password is missing')
        except Exception as er:
            messages.error(request, str(er))
        return redirect('login')        

def register(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'base/register.html', context)
    elif request.method == 'POST':
        email = request.POST.get('inputEmail', None)
        first_name = request.POST.get('inputFirstName', None)
        last_name = request.POST.get('inputLastName', None)
        password = request.POST.get('inputPassword', None)
        password_again = request.POST.get('inputPasswordAgain', None)
        try:
            if (email != None) and (first_name != None) and (last_name != None) and (password != None) and (password_again != None):
                if password == password_again:
                    wongnok_user_obj = base_models.WongnokUser(
                        email=email,
                        first_name=first_name,
                        last_name=last_name
                    )
                    wongnok_user_obj.set_password(password)
                    wongnok_user_obj.save()                    
                    messages.error(request, 'registration is success!')
                    return redirect('login')
                else:
                    messages.error(request, 'both passwords are not matched')
            else:
                messages.error(request, 'something is missing')
        except Exception as er:
            messages.error(request, str(er))
        return redirect('register')        

def logout_base(request):
    logout(request)
    return redirect('home')
