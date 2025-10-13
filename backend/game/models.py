from django.contrib.auth.models import User
from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Game: {self.name}"


class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, related_name='players', on_delete=models.CASCADE)
    spirit_name = models.CharField(max_length=50, blank=True, null=True)
