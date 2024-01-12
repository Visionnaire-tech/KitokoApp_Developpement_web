from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from usersapp.forms import UserRegistrationForm , TransertTP
from django.contrib.auth import login, authenticate
from django.contrib import messages

def register(request):
	if request.method == 'POST' :
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()		
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request,user)	
			messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')					
			return redirect('home')
	else :
		form = UserRegistrationForm()
	return render(request,'registration/register.html',{'form' : form})
def pdf(request):
    return render(request, 'pdf.html')

def envoistp(request):
    if request.method == 'POST':
        form = TransertTP(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'conf.html')
        else:
            return render(request,'conf.html')
    else:
        form = TransertTP()
        return render(request , 'envoistp.html' , {'form' : form})
    
def save(request):
    form = TransertTP(request.POST)
    if form.is_valid():
        form.save()
        return render (request,'conf.html')
    else:
        return render(request,'conf.html')   
def logout(request):
    
    return redirect(request,'login')


    