from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Game, Player
from .serializers import GameSerializer, RegisterSerializer, GameCreateSerializer


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


# Registration view
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer