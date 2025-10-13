from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from game.views import GameListAPIView, RegisterView, GameCreateAPIView, JoinGameAPIView

urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),


    path("games/", GameListAPIView.as_view(), name="games_list"),
    path('games/<int:pk>/join/', JoinGameAPIView.as_view(), name='game_join'),
    path('games/create/', GameCreateAPIView.as_view(), name='game_create'),

]