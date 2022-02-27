from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about', views.about, name='about'),
	path('contact', views.importance, name='importance'),
	path('future', views.goal, name='goal'),
	path('carbon', views.carbon, name='carbonEmpty'),
	path('carbon/<str:ip>', views.carbon, name='carbon')
]