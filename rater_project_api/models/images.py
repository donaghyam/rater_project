from django.db import models
from rater_project_api.models.players import Player
from rater_project_api.models.games import Games

class Images(models.Model):

    url = models.CharField(max_length=100)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    game = models.ForeignKey("Games", on_delete=models.CASCADE)