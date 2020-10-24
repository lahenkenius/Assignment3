from django.contrib import admin

from .models import Team, Game

class TeamList(admin.ModelAdmin):
    list_display = ('team_name', 'wins', 'losses')
    list_filter = ('team_name', 'wins')
    search_fields = ('team_name', )
    ordering = ['wins']

class GameList(admin.ModelAdmin):
    list_display = ('game_number', 'week_number', 'home_team_score','away_team_score', 'home_team,', 'away_team',
                    'winner', 'loser')
    list_filter = ('game_number', 'week_number', 'home_team_score','away_team_score', 'home_team,', 'away_team',
                   'winner', 'loser')
    #search_fields = ('game_number')
    #ordering = ['week_number']

admin.site.register(Team)
admin.site.register(Game)
