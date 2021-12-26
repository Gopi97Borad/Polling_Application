
from django.urls import path

from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('home/results/', views.results, name='results'),
    path('home/vote/', views.vote, name='vote'),
    path('home/delete/<int:task_id>', views.delete, name='delete'),
    path('home/update/<int:task_id>/<int:category_id>', views.update, name='update'),
    path('home/logout', views.logout_d, name='logout'),
    path('home/edittask/<int:task_id>', views.editTask, name='update_task')
]
