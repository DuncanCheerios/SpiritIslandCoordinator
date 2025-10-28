from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from game.views import GameListAPIView, RegisterView, GameCreateAPIView, JoinGameAPIView, MeAPIView, GameDetailView, \
    GameEventListCreateView, GameEventDetailView, FearCardListView, EventCardListView, InvaderCardListView

urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('me/', MeAPIView.as_view(), name='me'),

    path("games/", GameListAPIView.as_view(), name="games_list"),
    path('games/<int:pk>/', GameDetailView.as_view(), name='game_detail'),
    path('games/<int:pk>/join/', JoinGameAPIView.as_view(), name='game_join'),
    path('games/create/', GameCreateAPIView.as_view(), name='game_create'),

    path('games/<int:game_id>/events/', GameEventListCreateView.as_view(), name='game-event-list'),
    path('games/<int:game_id>/events/<int:pk>/', GameEventDetailView.as_view(), name='game-event-detail'),

    # Static card lists
    path('fearcards/', FearCardListView.as_view(), name='fear-card-list'),
    path('eventcards/', EventCardListView.as_view(), name='event-card-list'),
    path('invadercards/', InvaderCardListView.as_view(), name='invader-card-list'),

]