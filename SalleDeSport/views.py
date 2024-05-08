from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Membre, Cours, Activite, TypeAbonnement, ModePaiement, Seance
from .forms import MembreForm


def index(request, membre_id):
	membre = Membre.objects.get(pk = membre_id)
	if request.method == 'POST':
		form = MembreForm(request.POST, instance = membre)
		print(form)
		if form.is_valid():
			form.save()
			return redirect('SalleDeSport:index')


	context = {
		'membre': get_object_or_404(Membre, pk = membre_id),
	}
	return render(request, "FitFlow/index.html", context)

def home(request):
    context = {}
    return render(request, "FitFlow/home.html", context)

def about(request):
	context = {}
	return render(request, "FitFlow/about.html", context)

def coaches(request):
    context = {}
    return render(request, "FitFlow/coaches.html", context)

def schedule(request):
    context = {}
    return render(request, "FitFlow/schedule.html", context)

def contact_us(request):
	context = {}
	return render(request, "FitFlow/contact.html", context)


def planning(request, membre_id):
    membre = get_object_or_404(Membre, pk=membre_id)
    seances = Seance.objects.all()


    days = [["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]]
    for i in range(7):
        s = seances.filter(jour=str(i)).order_by('heureDebut')
        l = []
        for j in range(s.count()):
            l += [s[j]]
        days.append(l)
        #break
        #print(s)
        #print(s[0][0])

    
    print(days)

    days_labelles = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
    context = {'membre': membre, 'days': days, "days_labelles": days_labelles}
    return render(request, "FitFlow/planning.html", context)


@login_required
def profile(request, membre_id):
    membre = get_object_or_404(Membre, pk=membre_id)
    #cours = get_object_or_404(Cours, pk=1)
    form = MembreForm(instance=membre)
    if request.method == 'POST':
        membre1 = membre.email
        form = MembreForm(request.POST, instance=membre)
        if form.is_valid():
            print(membre1)
            print(form.data['email'])
            if membre1 != form.data['email']:
            	user = User.objects.get(email=membre1)
            	user.username = form.data['email']
            	user.email = form.data['email']
            	user.save()
            form.save()
            return redirect('SalleDeSport:index', membre_id=membre_id)

    context = {'form': form, 'membre': membre}
    return render(request, "FitFlow/profile.html", context)

@login_required
def courses(request, membre_id):
	membre = get_object_or_404(Membre, pk=membre_id)
	cours = Cours.objects.all().order_by("activite")
	coursInscrits = membre.coursInscrits.all()
	print("Liste des cours : ",cours)
	print("Cours Inscrits :",coursInscrits)
	context = {'membre': membre, 'cours': cours, 'coursInscrits': coursInscrits}
	return render(request, "FitFlow/courses.html", context)

@login_required
def course(request,membre_id, cour_id):
	cour = get_object_or_404(Cours, pk=cour_id)
	membre = get_object_or_404(Membre, pk=membre_id)
	context = {'cour': cour,'membre': membre}
	return render(request, "FitFlow/course.html", context)

@login_required
def inscription(request, membre_id, cour_id):
    membre = get_object_or_404(Membre, pk=membre_id)
    cour = get_object_or_404(Cours, pk=cour_id)
    context = {'membre': membre}
    # Vérifier la capacité du cours
    if cour.capacite > cour.membres.count():
        # Ajouter le membre au cours
        cour.membres.add(membre)
        membre.save()
        return redirect('SalleDeSport:index', membre_id=membre_id)



def change_password(request, membre_id):
    membre = get_object_or_404(Membre, pk=membre_id)
    
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('password1')
        confirm_new_password = request.POST.get('password2')
        
        # Vérifier si le mot de passe actuel est correct
        if request.user.check_password(current_password):
            # Vérifier si les deux nouveaux mots de passe correspondent
            if new_password == confirm_new_password:
                # Modifier le mot de passe de l'utilisateur
                u = User.objects.get(username=membre.email)
                u.set_password(new_password)
                u.save()
                update_session_auth_hash(request, u)
                return redirect('SalleDeSport:index', membre_id=membre_id)
            else:
            	return redirect('account:edit_password', membre_id=membre_id)
                
        else:
            context = {'membre': membre, 'message': "Le mot de passe actuel est incorrect"}
            return render(request, "account/edit_password.html", context)
    
    return redirect('account:edit_password', membre_id=membre_id)

def list_abonnement(request, membre_id):
    membre = get_object_or_404(Membre, pk=membre_id)
    abonnements = TypeAbonnement.objects.all()
    # Récupérer les avantages pour chaque abonnement
    avantages_par_abonnement = {}
    for abonnement in abonnements:
        avantages = abonnement.avantages.splitlines()
        avantages_par_abonnement[abonnement.id] = avantages
    context = {'membre': membre, 'abonnements': abonnements, 'avantages_par_abonnement': avantages_par_abonnement}
    return render(request, "FitFlow/list_abonnement.html", context)

def payment(request, membre_id, abonnement_id):
    membre = get_object_or_404(Membre, pk=membre_id)
    abonnement = get_object_or_404(TypeAbonnement, pk=abonnement_id)
    avantages = abonnement.avantages.splitlines()
    context = {'membre': membre, 'abonnement': abonnement, 'avantages': avantages}    
    return render(request, "FitFlow/payment.html", context)

def choice_mode_paiement(request, membre_id, abonnement_id):
    membre = get_object_or_404(Membre, pk=membre_id)
    abonnement = get_object_or_404(TypeAbonnement, pk=abonnement_id)
    avantages = abonnement.avantages.splitlines()
    context = {'membre': membre, 'abonnement': abonnement, 'avantages': avantages}
    return render(request, "FitFlow/choice_mode_paiement.html", context)

def info_abonnement(request, membre_id, abonnement_id):
    membre = get_object_or_404(Membre, pk=membre_id)
    abonnement = get_object_or_404(TypeAbonnement, pk=abonnement_id)
    avantages = abonnement.avantages.splitlines()
    quatres_derniers_chiffres = str(membre.modePaiement.numeroCarte)[-4:]
    context = {'membre': membre, 'abonnement': abonnement, 'avantages': avantages, 'quatres_derniers_chiffres': quatres_derniers_chiffres}    
    return render(request, "FitFlow/info_abonnement.html", context) 


def valider_payement(request, membre_id, abonnement_id):
    membre = get_object_or_404(Membre, pk=membre_id)
    abonnement = get_object_or_404(TypeAbonnement, pk=abonnement_id)
    if request.method == 'POST':
        nom = request.POST.get('holdername')
        num_carte = request.POST.get('cardno')
        cvc = request.POST.get('cvcpwd')
        dateExp = request.POST.get('exp')

        mode_paiement = ModePaiement.objects.create(
                    titulaire = nom,
                    numeroCarte = num_carte,
                    cvc = cvc,
                    dateExp = dateExp,
                    )

        membre.modePaiement = mode_paiement
        membre.typeAbon = abonnement

        membre.save()

    else:
        print(True)
        membre.typeAbon = abonnement
        membre.save()

    context = {'membre': membre}
    return render(request, "FitFlow/index.html", context)

def list_seances(request, membre_id):
    membre = get_object_or_404(Membre, pk=membre_id)
    seances = Seance.objects.all()
    print("Hello")
    context = {'membre': membre, 'seances': seances}
    return render(request, "FitFlow/liste_seances.html", context)

def reserver(request, membre_id, seance_id):
    membre = get_object_or_404(Membre, pk=membre_id)
    seance = get_object_or_404(Seance, pk=seance_id)
    context = {'membre': membre}
    # Vérifier la capacité du cours
    if seance.cours.capacite > seance.seances.count():
        # Ajouter le membre au cours
        seance.seances.add(membre)
        membre.save()
        return redirect('SalleDeSport:index', membre_id=membre_id)

