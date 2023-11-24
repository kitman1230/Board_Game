"""Defines URL patterns for game_board."""

from django.urls import path
from . import views

app_name = "game_board"
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    path("boardgames/", views.boardgames, name="boardgames"),
    path("boardgames/<int:boardgame_id>/", views.boardgame, name="boardgame"),
    path("new_boardgame/", views.new_boardgame, name="new_boardgame"),
    path("boardgame/<int:boardgame_id>/", views.edit_boardgame, name="edit_boardgame"),
    path(
        "remove_boardgame/<int:boardgame_id>/",
        views.remove_boardgame,
        name="remove_boardgame",
    ),
    path("new_comment/<int:boardgame_id>/", views.new_comment, name="new_comment"),
    path("edit_comment/<int:comment_id>/", views.edit_comment, name="edit_comment"),
    path("categories/", views.categories, name="categories"),
    path("categories/<int:category_id>/", views.category, name="category"),
    path("profile/", views.profile, name="profile"),
    path("update_profile/", views.update_profile, name="update_profile"),
    path("lend/<int:boardgame_id>/", views.lend, name="lend"),
    path("lendreturn/<int:loanrecord_id>/", views.lendreturn, name="lendreturn"),
    path("lendstatics/", views.lendstatics, name="lendstatics"),
    path("lendhistory/<int:boardgame_id>/", views.lendhistory, name="lendhistory"),
]
