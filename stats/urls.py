from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('players/', views.player_stats, name='player_stats'),
    path('team/<int:team_id>/', views.team_detail, name='team_detail'),
]