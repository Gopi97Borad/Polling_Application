
from django.urls import path

from . import views


urlpatterns = [
    path('', views.login, name='login'),
    #path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('home/results/', views.results, name='results'),
    path('home/vote/', views.vote, name='vote'),
]
