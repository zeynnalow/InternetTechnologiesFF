from django.contrib import admin
from .models import Team, Player, Match

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    search_fields = ('name',)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'team', 'goals', 'assists', 'total_points')
    list_filter = ('team',)
    search_fields = ('first_name', 'last_name')
    
    def total_points(self, obj):
        return obj.goals + obj.assists
    total_points.short_description = 'G+A Contribution'

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('home_team', 'home_score', 'away_score', 'away_team', 'date')