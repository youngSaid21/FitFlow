from django.contrib import admin
from .models import *

class ModelMembre(admin.ModelAdmin):
	list_display = ('nom', 'prenom', 'email', 'tel', 'preferenceNotif','dateRenouvellement',)
	list_filter = ['typeAbon',]
	search_fields = ('nom','prenom')
	list_per_page = 20

	fieldsets = [
		('Informations Personnelles', {'fields': ['nom', 'prenom', 'email', 'tel']}),
		("Abonnement et Paiement", {'fields': ['dateRenouvellement','typeAbon','modePaiement','preferenceNotif']}),
	]

	inlines = [
    	MembershipInline,
    	ReservationCoursInline,
    ]
	exclude = ["seancesReserves"]

class ModelInvite(admin.ModelAdmin):
	list_display = ('nom', 'prenom', 'email', 'tel','seanceEssai')
	search_fields = ('nom','prenom')
	list_per_page = 20

	fieldsets = [
		('Informations personnelles', {'fields': ['nom', 'prenom', 'email', 'tel']}),
		("Séance d'essai", {'fields': ['seanceEssai']}),
	]


class ModelSeance(admin.ModelAdmin):


	list_display = ('cours','heureDebut','jour')
	list_per_page = 20
	fieldsets = [
		('Planification', {'fields': ['cours','heureDebut','jour']}),
	]
	inlines = [
    	ReservationCoursInline,
    ]
	


class ModelTypeAbonnement(admin.ModelAdmin):
	list_display = ('nomAbon', 'dureAbon', 'prixAbon','description', 'avantages')
	list_filter = ('nomAbon',)
	list_per_page = 20

	fieldsets = [
		("Type d'abonnement", {'fields': ['nomAbon', 'dureAbon', 'prixAbon','description', 'avantages']}),
	]

class ModelInstructeur(admin.ModelAdmin):
	list_display = ('nom', 'prenom', 'email', 'tel',)
	search_fields = ('nom','prenom')
	list_per_page = 20

	fieldsets = [
		('Informations personnelles', {'fields': ['nom', 'prenom', 'email', 'tel']}),
	]

class ModelEquipement(admin.ModelAdmin):
	list_display = ('nomEquip', 'dateAchat', 'dureeVie','quantity','club')
	list_filter = ('nomEquip','club')
	list_per_page = 20

	fieldsets = [
		('Équipements', {'fields': ['nomEquip', 'dateAchat', 'dureeVie','quantity','club']}),
	]

class ModelClub(admin.ModelAdmin):
	list_display = ('nomClub', 'email', 'tel','addressClub','ville')
	list_filter = ('nomClub','ville')
	search_fields = ('email',)
	list_per_page = 20
	inlines = [ClubActiviteInline]

	fieldsets = [
		('Informations du club', {'fields': ['nomClub', 'email', 'tel','addressClub','ville']}),
	]

	class Meta:
		model = Club

class ModelActivite(admin.ModelAdmin):
	list_display = ('nomAcitivite', 'DescActivite',)
	search_fields = ('nomAcitivite',)
	list_per_page = 20
	inlines = [ClubActiviteInline]

	fieldsets = [
		("Informations de l'activité", {'fields': ['nomAcitivite', 'DescActivite',]}),
	]

	class Meta:
		model = Activite

class ModelCours(admin.ModelAdmin):
	list_display = ['nomCours','capacite','description','instructeur','activite']
	search_fields = ('nomCours',)
	list_filter = ('instructeur','activite')

	inlines = [
    	MembershipInline,
    ]

class ModePaiementModel(admin.ModelAdmin):
	list_display = ('titulaire','numeroCarte','dateExp','cvc')

	fieldsets = [
		('Mode de Paiement', {'fields': ['titulaire','numeroCarte','dateExp','cvc']}),
	]

admin.site.register(Membre,ModelMembre)
admin.site.register(TypeAbonnement, ModelTypeAbonnement)
admin.site.register(Instructeur, ModelInstructeur)
admin.site.register(Invite,ModelInvite)
admin.site.register(Seance, ModelSeance)
admin.site.register(Activite, ModelActivite)
admin.site.register(Club, ModelClub)
admin.site.register(Equipement, ModelEquipement)
admin.site.register(Cours,ModelCours)
admin.site.register(ModePaiement, ModePaiementModel)
