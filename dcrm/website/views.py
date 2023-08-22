from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # Se comprueba si el usuario se ha logeado
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Autenticar los datos
        user = authenticate(request, username = username, password = password)
        
        if user != None:
            login(request, user)
            messages.success(request, "Te has logueado")
            return redirect('home')
        else:
            messages.success(request, 'Ha ocurrido un error, pruebe de nuevo')
            return redirect('home')
            
    else:
        return render(request, 'home.html', {})

#def login_user(request):
#    pass

def logout_user(request):
    logout(request)
    messages.success(request, "Te has deslogueado")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})