from django.db import models

# Create your models here.
class Team(models.Model):
    team_name = models.CharField(max_length=50, primary_key=True)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    def __str__(self):
        return str(self.team_name)


class Game(models.Model):
     game_number=models.AutoField(primary_key=True)
     week_number = models.IntegerField(default=1)
     home_team_score=models.IntegerField(default=0)
     away_team_score=models.IntegerField(default=0)
     home_team = models.CharField(max_length=50, blank=True, null=True)
     away_team = models.CharField(max_length=50, blank=True, null=True)
     winner = models.CharField(max_length=50, blank=True, null=True)
     loser = models.CharField(max_length=50, blank=True, null=True)

     def __str__(self):
         return str(self.game_number)

