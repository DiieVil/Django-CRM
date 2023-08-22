from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

def home(request):
    # Se obtienen todos los datos de records
    records = Record.objects.all()
    
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
    # Si el usuario ya esta logueado
    else:
        return render(request, 'home.html', {'records':records})

#def login_user(request):
#    pass

def logout_user(request):
    logout(request)
    messages.success(request, "Te has deslogueado")
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Te has registrado correctamente")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
	if request.user.is_authenticated:
		# Se ve el record del usuario seleccionado
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "Tienes que estar logueado para ver esta pagina")
		return redirect('home')


def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Registro borrado correctamente")
		return redirect('home')
	else:
		messages.success(request, "Tienes que estar registrado para hacer la acción")
		return redirect('home')


def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Registro añadido")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "Tienes que estar registrado")
		return redirect('home')

def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "El registro ha sido actualizado")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "Tienes que estar registrado para realizar la acción")
		return redirect('home')