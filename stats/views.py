from django.shortcuts import render, get_object_or_404
from .models import Team, Player, Match

def home(request):
    teams = Team.objects.all()
    recent_matches = Match.objects.all().order_by('-date')[:5]
    return render(request, 'stats/home.html', {'teams': teams, 'matches': recent_matches})

def player_stats(request):
    top_scorers = Player.objects.select_related('team').order_by('-goals')[:10]
    top_assists = Player.objects.select_related('team').order_by('-assists')[:10]
    
    return render(request, 'stats/players.html', {
        'top_scorers': top_scorers,
        'top_assists': top_assists
    })

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    players = team.players.all().order_by('-goals')
    return render(request, 'stats/team_detail.html', {'team': team, 'players': players})


def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    squad = team.players.all().order_by('-goals') 
    
    return render(request, 'stats/team_detail.html', {
        'team': team,
        'squad': squad
    })