from django.db import models

class Position(models.Model):
    name = models.CharField(max_length=50, unique=True) # GK, CB, ST və s.
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    positions = models.ManyToManyField(Position) # Bir oyunçu bir neçə mövqedə oynaya bilər
    goals = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    goals_conceded = models.PositiveIntegerField(default=0, verbose_name="Goals Conceded (For GK)")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.team.name})"

class Match(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    squad = models.ManyToManyField(Player, related_name='matches_played', blank=True)

    def __str__(self):
        return f"{self.home_team.name} {self.home_score}-{self.away_score} {self.away_team.name}"

class GoalScorer(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='goals_scored')
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    minute = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.player.last_name} - {self.match}"