# coding: utf-8

from django.db import models
from django.contrib import admin
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Personne(models.Model):
	nom  	= models.CharField(max_length = 32, null = False, verbose_name = 'Nom')
	prenom  = models.CharField(max_length = 64, null = False, verbose_name = 'Prénom')
	email 	= models.EmailField(max_length = 64, unique = True, null = False,  verbose_name = 'Email')
	tel 	= PhoneNumberField(blank=False, null = False, unique = True, verbose_name = 'Téléphone') 

	class Meta:
		abstract = True


class TypeAbonnement(models.Model):
	nomAbon 			 = models.CharField(max_length = 24, unique = True, null = False, verbose_name = "Nom de l'abonnenment")
	dureAbon			 = models.PositiveIntegerField(null = False, verbose_name = "Durée (en mois)")
	prixAbon			 = models.PositiveIntegerField(null = False, verbose_name = 'Prix')

	def __str__(self):
		return self.nomAbon

	class Meta:
		verbose_name = "Type d'abonnement"
		verbose_name_plural = "Types d'abonnement"
		db_table = 'typeabonnement'

class ModePaiement(models.Model):
	cartes 				= [
						    ("Ma", "Mastercard"),
						    ("Vi", "Visa"),
	]
	typeCarte 			= models.CharField(max_length = 24, null = False, verbose_name = "Type du Carte", choices = cartes)
	numeroCarte			= models.PositiveBigIntegerField(null = False, verbose_name = "Numéro de la carte")
	dateExp			 	= models.DateField(verbose_name = "Date d'expiration")
	cvc 				= models.PositiveSmallIntegerField(null = False, verbose_name = 'CVC') 
	address 			= models.CharField(max_length = 86,null = False, verbose_name = 'Adresse de facturation') 

	def __str__(self):
		return str(self.numeroCarte)

	class Meta:
		verbose_name = "Mode de paiement"
		verbose_name_plural = "Modes de paiement"
		db_table = 'modepaiment'


class Instructeur(Personne):

	def __str__(self):
		return f"{self.prenom} {self.nom}"

	class Meta:
		verbose_name = 'Instructeur'
		verbose_name_plural = 'Instructeurs'
		db_table = 'instructeur'

class Activite(models.Model):
	nomAcitivite = models.CharField(max_length = 32, unique = True, null = False, verbose_name = 'Nom')
	DescActivite = models.CharField(max_length = 64, null = False, verbose_name = 'Description')


	class Meta:
		verbose_name = 'Activité'
		verbose_name_plural = 'Activités'
		db_table = 'activite'

	def __str__(self):
		return self.nomAcitivite
	
	def __unicode__(self):
		return self.nomAcitivite

class Cours(models.Model):
	nomCours = models.CharField(max_length = 32, unique = True, null = False, verbose_name = 'Nom')
	capacite = models.PositiveIntegerField(null = False, verbose_name = 'Capacité')
	description = models.CharField(max_length = 64, null = False, verbose_name = 'Description')
	instructeur = models.ForeignKey(Instructeur, on_delete = models.CASCADE, verbose_name = 'Instructeur')
	activite = models.ForeignKey(Activite, on_delete = models.CASCADE, verbose_name = 'Activité')


	def __str__(self):
		return self.nomCours

	class Meta:
		verbose_name = 'Cours'
		verbose_name_plural = 'Cours'
		db_table = 'cours'

class Club(models.Model):
	nomClub 	= models.CharField(max_length = 24, unique = True, null = False, verbose_name = 'Nom')
	email 		= models.EmailField(max_length = 64, unique = True, null = False, verbose_name = 'Email')
	tel 		= PhoneNumberField(blank=True, unique = True, null = False, verbose_name = 'Téléphone') 
	addressClub = models.CharField(max_length = 64, unique = True, null = False,  verbose_name = 'Adresse')
	activites 	= models.ManyToManyField(Activite, related_name = 'clubs', blank=True)
	villes 		= [
		    ("Ag", "Agadir"),
		    ("Ca", "Casablanca"),
		    ("Mar", "Marakech"),
		    ("Ra", "Rabat"),
		    ("Tg", "Tanger"),
	]
	ville		= models.CharField(max_length = 64, null = False,  verbose_name = 'Ville', choices = villes)

	class Meta:
		verbose_name = 'Club'
		verbose_name_plural = 'Clubs'
		db_table = 'club'
		unique_together = ('nomClub', 'ville')

	

	def __str__(self):
		return self.nomClub

class Equipement(models.Model):
	nomEquip 	= models.CharField(max_length = 32, null = False, verbose_name = 'Nom')
	dateAchat 	= models.DateField(null = False, verbose_name = "Date d'achat")
	dureeVie 	= models.PositiveIntegerField(verbose_name = "Durée de vie")
	quantity 	= models.PositiveIntegerField(null = False, verbose_name = "Quantité")
	club 		= models.ForeignKey(Club, on_delete = models.CASCADE, verbose_name = 'Club')

	def __str__(self):
		return self.nomEquip

	class Meta:
		verbose_name = 'Equipement'
		verbose_name_plural = 'Equipements'
		db_table = 'equipement'
		unique_together = ('nomEquip', 'club')

class ClubActiviteInline(admin.TabularInline):
	#fk_name = models.ForeignKey(Activite)
	model = Club.activites.through
	#filter_vertical = ("activite",)
	extra = 0
	#raw_id_fields = ['nomClub','nomAcitivite']

	class Meta:
		verbose_name = "Club et activ***)"

class Seance(models.Model):
	cours 		= models.ForeignKey(Cours, on_delete = models.CASCADE, verbose_name = 'Cours')
	dateCours 	= models.DateField(verbose_name = "Date de la séance")
	heureDebut 	= models.TimeField(verbose_name = "Début de la séance")
	heureFin 	= models.TimeField(verbose_name = "Fin de la séance")

	def __str__(self):
		return self.cours.nomCours

	class Meta:
		verbose_name = 'Séance'
		verbose_name_plural = "Séances"
		db_table = 'seanceEssai'

class Membre(Personne):
	preferenceNotif 	= models.BooleanField(verbose_name = 'Notification')
	dateRenouvellement	= models.DateField(blank = True, null=True, verbose_name = 'Date du Renouvellement')
	typeAbon 			= models.ForeignKey(TypeAbonnement, on_delete = models.CASCADE, null=True, blank=True, verbose_name = "Type d'abonnement")
	modePaiement 		= models.ForeignKey(ModePaiement, on_delete = models.CASCADE, null=True, blank=True,  verbose_name = "Mode de paiement")
	coursInscrits 		= models.ManyToManyField(Cours, related_name = 'membres', verbose_name = 'Cours Inscrits', blank=True)
	seancesReserves 	= models.ManyToManyField(Seance, related_name  = 'seances', verbose_name = 'Séances resérvées', blank=True)


	def __str__(self):
		return f"{self.prenom} {self.nom}"

	class Meta:
		verbose_name = 'Membre'
		verbose_name_plural = 'Membres'
		db_table = 'membre'


class MembershipInline(admin.TabularInline):
    model = Membre.coursInscrits.through

'''class ReservationCour(models.Model):
    seance = models.ForeignKey(Seance, on_delete=models.CASCADE, default = 1)
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    
    def annuler_reservation(self):
    	pass'''

class ReservationCoursInline(admin.TabularInline):
	model = Membre.seancesReserves.through
	
class Invite(Personne):
	seanceEssai = models.ForeignKey(Seance, on_delete = models.CASCADE, null=True, blank=True, verbose_name = "Séance d'essai")	

	def __str__(self):
		return f"{self.prenom} {self.nom}"

	class Meta:
		verbose_name = 'Invité'
		verbose_name_plural = 'Invités'
		db_table = 'invite'



