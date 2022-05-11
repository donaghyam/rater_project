from django.db import models
from rater_project_api.models.players import Player
from rater_project_api.models.categories import Categories



class Games(models.Model):

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    designer = models.CharField(max_length=50)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    estimated_time_to_play = models.IntegerField()
    age_recommendation = models.CharField(max_length=10)
    player = models.ForeignKey("Player", on_delete=models.CASCADE),
    categories=models.ManyToManyField("Categories", related_name="categories")
    