from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    # mian page
    path("", views.index, name="index"),

    # User
    path("kidedu/log_in/", views.log_in, name="log_in"),
    path("kidedu/sign_up/", views.register, name="sign_up"),
    path("kidedu/log_out/", views.log_out, name="log_out"),

    # Article views
    path("kidedu/article", views.articles, name="articles"),
    path("kidedu/article/<int:id>/view_page",
         views.view_page, name="view_page"),
    path('kidedu/article/<int:id>/comment',
         views.comments, name='comments'),

    # Games Pages
    path('kidedu/games', views.games, name="games"),
    path('kidedu/games/Memory_card', views.game_1, name="game_1"),
    path('kidedu/games/colors', views.colors, name="colors"),

]
