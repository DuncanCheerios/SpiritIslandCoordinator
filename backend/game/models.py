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

class GameEvent(models.Model):
    EVENT_TYPES = [
        ('fear', 'Fear Card'),
        ('event', 'Event Card'),
        ('invader', 'Invader Card'),
        ('blight', 'Blighted Island'),
        ('custom', 'Custom'),
    ]

    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='events')
    type = models.CharField(max_length=20, choices=EVENT_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    # optional foreign keys depending on type
    fear_card = models.ForeignKey('FearCard', null=True, blank=True, on_delete=models.SET_NULL)
    event_card = models.ForeignKey('EventCard', null=True, blank=True, on_delete=models.SET_NULL)
    invader_card = models.ForeignKey('InvaderCard', null=True, blank=True, on_delete=models.SET_NULL)

    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        label = (
            self.fear_card.name
            if self.type == 'fear' and self.fear_card
            else self.event_card.name
            if self.type == 'event' and self.event_card
            else self.title
        )
        return f"[{self.get_type_display()}] {label or 'Unnamed'}"


class FearCard(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class InvaderCard(models.Model):
    name = models.TextField(max_length=200)
    stage = models.IntegerField()
    escalation = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class EventCard(models.Model):
    name = models.TextField(max_length=200)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name