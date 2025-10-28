from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Game, Player, FearCard, EventCard, InvaderCard, GameEvent


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


class FearCardSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None

    class Meta:
        model = FearCard
        fields = ['id', 'name', 'description', 'image_url', 'last_updated', 'stage_one', 'stage_two', 'stage_three']


class EventCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCard
        fields = ['id', 'name', 'description', 'image_url', 'last_updated']


class InvaderCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvaderCard
        fields = ['id', 'name', 'stage', 'escalation']


class GameEventSerializer(serializers.ModelSerializer):
    # Nested read-only serializers for display
    fear_card = FearCardSerializer(read_only=True)
    event_card = EventCardSerializer(read_only=True)
    invader_card = InvaderCardSerializer(read_only=True)

    title = serializers.SerializerMethodField()

    def get_title(self, obj):
        if obj.fear_card:
            return obj.fear_card.name + (" Level: " + obj.terror_level if obj.terror_level else "")
        elif obj.event_card:
            return obj.event_card.name
        elif obj.invader_card:
            return obj.invader_card.name + " " + str(obj.invader_card.stage)
        else:
            return obj.title

    fear_card_id = serializers.PrimaryKeyRelatedField(
        queryset=FearCard.objects.all(),
        source='fear_card',
        write_only=True,
        required=False
    )
    event_card_id = serializers.PrimaryKeyRelatedField(
        queryset=EventCard.objects.all(),
        source='event_card',
        write_only=True,
        required=False
    )
    invader_card_id = serializers.PrimaryKeyRelatedField(
        queryset=InvaderCard.objects.all(),
        source='invader_card',
        write_only=True,
        required=False
    )

    class Meta:
        model = GameEvent
        fields = [
            'id',
            'game_id',
            'type',
            'title',
            'description',
            'fear_card',
            'fear_card_id',
            'terror_level',
            'event_card',
            'event_card_id',
            'invader_card_id',
            'invader_card',
            'created_at',
        ]
