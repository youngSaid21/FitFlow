from django.urls import path
from . import views

app_name = "SalleDeSport"

urlpatterns = [
	path('<int:membre_id>/', views.index, name ='index'),
	path('', views.home, name = 'home'),
	path('contact', views.contact, name = 'contact'),
	path('planning', views.planning, name = 'planning'),
]