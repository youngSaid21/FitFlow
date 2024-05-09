from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from SalleDeSport.models import Membre

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            membre = Membre.objects.all().filter(email=username)
            auth.login(request, user)
            return redirect('SalleDeSport:index', membre_id = membre[0].id )
        else:
            messages.error(request, 'Invalid login details')
    
    return render(request, 'account/login.html', {'form': LoginForm})

def logout(request):
    auth.logout(request)
    messages.info(request, 'You have been logged out!!')
    
    return redirect('SalleDeSport:home')

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)

		if form.is_valid():
			last_name = form.data['last_name']
			first_name = form.data['first_name']
			email = form.data['email']
			phone = form.data['phone']
			password1 = form.data['password1']
			password2 = form.data['password2']

			if password1 == password2:

				user = User.objects.create_user(email, email, password1)
				user.save()

				Membre.objects.create(
					nom = last_name,
					prenom = first_name,
					email = email,
					tel = phone,
					preferenceNotif = False,
					)

				return redirect("account:login")

	else:
		form = RegistrationForm()

	return render(request, "account/register.html", {"form": form})


def edit_password(request, membre_id):
	membre = get_object_or_404(Membre, pk=membre_id)
	return render(request, "account/edit_password.html", {'membre': membre, 'message': ''})



