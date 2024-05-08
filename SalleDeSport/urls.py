from django.urls import path
from . import views

app_name = "SalleDeSport"

urlpatterns = [
	path('<int:membre_id>/', views.index, name ='index'),
	path('', views.home, name = 'home'),
	path('about', views.about, name = 'about'),
	path('coaches', views.coaches, name = 'coaches'),
	path('schedule', views.schedule, name = 'schedule'),
	path('contact_us', views.contact_us, name = 'contact_us'),
	path('<int:membre_id>/planning', views.planning, name = 'planning'),
	path('profile/<int:membre_id>', views.profile, name = 'profile'),
	path('courses/<int:membre_id>', views.courses, name = 'courses'),
	path('courses/<int:membre_id>/course/<int:cour_id>', views.course, name = 'course'),
	path('inscription/<int:membre_id>/<int:cour_id>', views.inscription, name = 'inscription'),
	path('change_password/<int:membre_id>', views.change_password, name='change_password'),
	path('<int:membre_id>/list_abonnement', views.list_abonnement, name = 'list_abonnement'),
	path('<int:membre_id>/list_abonnement/<int:abonnement_id>/payment', views.payment, name = 'payment'),	
	path('<int:membre_id>/valider_payement/<int:abonnement_id>', views.valider_payement, name='valider_payement'),
	path('<int:membre_id>/list_abonnement/<int:abonnement_id>/choice_mode_paiement', views.choice_mode_paiement, name = 'choice_mode_paiement'),
	path('<int:membre_id>/list_abonnement/<int:abonnement_id>/info_abonnement', views.info_abonnement, name = 'info_abonnement'),
	path('<int:membre_id>/list_seances', views.list_seances, name = 'list_seances'),
	path('reserver/<int:membre_id>/<int:seance_id>', views.reserver, name = 'reserver'),

]