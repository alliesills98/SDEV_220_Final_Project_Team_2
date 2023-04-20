from django.urls import path
from . import views

urlpatterns = [
    #Use path converter of int and str to create month and year url name within the path
    path('', views.index, name="index"),
    path('<int:year>/<str:month>/', views.index, name="index"),
    path('games', views.all_games, name="list-games"),
]