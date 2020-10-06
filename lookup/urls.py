from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcomepage'),
    path('home', views.home, name='home'),
    path('about.html', views.about, name='about'),
]
