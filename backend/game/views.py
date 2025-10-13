from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Game
from .serializers import GameSerializer, RegisterSerializer


class GameListAPIView(generics.ListAPIView):
    queryset = Game.objects.all().order_by('-date_created')  # newest first
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]


# Registration view
class RegisterView(generics.CreateAPIView):
    print('hihihi')
    serializer_class = RegisterSerializer