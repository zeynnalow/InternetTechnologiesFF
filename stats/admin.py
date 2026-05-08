from django.contrib import admin
from .models import Team, Player, Match, Position, GoalScorer

class GoalScorerInline(admin.TabularInline):
    model = GoalScorer
    extra = 2 # Boş qol vuran sətirlərinin sayı

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('home_team', 'home_score', 'away_score', 'away_team', 'date')
    inlines = [GoalScorerInline]
    filter_horizontal = ('squad',) # Heyəti asan seçmək üçün widget

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'team', 'goals', 'goals_conceded')
    list_filter = ('team', 'positions')
    filter_horizontal = ('positions',)

admin.site.register(Team)
admin.site.register(Position)