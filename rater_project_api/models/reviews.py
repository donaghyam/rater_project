from django.db import models
from rater_project_api.models.players import Player
from rater_project_api.models.games import Games


class Review(models.Model):

    review = models.CharField(max_length=200)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    game = models.ForeignKey("Games", on_delete=models.CASCADE)