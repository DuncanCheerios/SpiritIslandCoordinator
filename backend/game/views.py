from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Game, Player, GameEvent, FearCard, EventCard, InvaderCard
from .serializers import GameSerializer, RegisterSerializer, GameCreateSerializer, GameEventSerializer, \
    FearCardSerializer, EventCardSerializer, InvaderCardSerializer


class GameCreateAPIView(generics.CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Set the creator
        game = serializer.save(created_by=self.request.user)
        # Add creator as first player
        Player.objects.create(user=self.request.user, game=game)


class JoinGameAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            print(pk)
            game = Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            return Response({"detail": "Game not found"}, status=status.HTTP_404_NOT_FOUND)

        # Check if user is already in the game
        if Player.objects.filter(user=request.user, game=game).exists():
            return Response({"detail": "Already joined"}, status=status.HTTP_400_BAD_REQUEST)

        # Add the user to the game
        Player.objects.create(user=request.user, game=game)
        return Response({"detail": "Joined successfully"}, status=status.HTTP_201_CREATED)


class GameListAPIView(generics.ListAPIView):
    queryset = Game.objects.all().order_by('-date_created')  # newest first
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]


class GameDetailView(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


# Registration view
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class MeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
        })


class GameEventListCreateView(generics.ListCreateAPIView):
    serializer_class = GameEventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return GameEvent.objects.filter(game_id=self.kwargs['game_id']).order_by('created_at')

    def perform_create(self, serializer):
        print('supsupsup')
        serializer.save(game_id=self.kwargs['game_id'])


# Optional detail view (GET /api/games/<id>/events/<event_id>/)
class GameEventDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GameEventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return GameEvent.objects.filter(game_id=self.kwargs['game_id'])


# Static lists for frontend dropdowns
class FearCardListView(generics.ListAPIView):
    queryset = FearCard.objects.all().order_by('name')
    serializer_class = FearCardSerializer
    permission_classes = [IsAuthenticated]


class EventCardListView(generics.ListAPIView):
    queryset = EventCard.objects.all().order_by('name')
    serializer_class = EventCardSerializer
    permission_classes = [IsAuthenticated]


class InvaderCardListView(generics.ListAPIView):
    queryset = InvaderCard.objects.all().order_by('name')
    serializer_class = InvaderCardSerializer
    permission_classes = [IsAuthenticated]
