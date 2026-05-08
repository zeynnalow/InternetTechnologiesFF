from django.shortcuts import render, get_object_or_404
from .models import Team, Player, Match

def home(request):
    teams = Team.objects.all()
    recent_matches = Match.objects.all().order_by('-date')[:3] # Sadece son 3 matç
    return render(request, 'stats/home.html', {'teams': teams, 'matches': recent_matches})

def all_matches(request):
    matches = Match.objects.all().order_by('-date')
    return render(request, 'stats/all_matches.html', {'matches': matches})

def match_detail(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    scorers = match.goals_scored.all().order_by('minute')
    squad = match.squad.all()
    return render(request, 'stats/match_detail.html', {'match': match, 'scorers': scorers, 'squad': squad})

def player_stats(request):
    top_scorers = Player.objects.order_by('-goals')[:10]
    # Qapıçılar (GK mövqeyi olanlar) buraxdıqları qola görə
    goalkeepers = Player.objects.filter(positions__name="GK").order_by('goals_conceded')
    return render(request, 'stats/players.html', {'top_scorers': top_scorers, 'goalkeepers': goalkeepers})

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    players = team.players.all().order_by('-goals')
    return render(request, 'stats/team_detail.html', {'team': team, 'players': players})