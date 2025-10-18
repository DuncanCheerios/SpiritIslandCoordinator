from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Game, Player


class GameCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['name']


class PlayerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Player
        fields = ['user', 'game', 'username']

class GameSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)  # nested players

    class Meta:
        model = Game
        fields = ['id', 'name', 'date_created', 'players']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
