from django.urls import path
from . import views

urlpatterns = [
    #Use path converter of int and str to create month and year url name within the path
    #main page
    path('', views.index, name="index"),
    path('<int:year>/<str:month>/', views.index, name="index"),

    #games
    path('add_game/',views.add_game,name="add-game"),
    path('join_game/',views.join_game, name = "join-game"),
    path('search_games/',views.search_games,name="search-games"),
    path('games/', views.all_games, name="list-games"),
    path('show_game/<game_id>', views.show_game, name="show-game"),
    path('update_game/<game_id>', views.update_game, name="update-game"),
    path('delete_game/<game_id>', views.delete_game,name='delete-game'),

    #rooms
   
    path('rooms/', views.all_rooms, name="list-rooms"),
    path('show_room/<room_id>', views.show_room, name="show-room"),
   
]