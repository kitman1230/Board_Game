from django.shortcuts import render, redirect
from .models import BoardGame, Category, Comment, Category, LoanRecord
from .forms import BoardGameForm, CommentForm, ProfileForm, LoanRecordForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
def index(request):
    """The home page for Game Board."""
    return render(request, "game_board/index.html")


def boardgames(request):
    """Show all board games"""
    boardgames = BoardGame.objects.order_by("-date_added")
    context = {"boardgames": boardgames}
    return render(request, "game_board/boardgames.html", context)


def boardgame(request, boardgame_id):
    """Show a single board game and all its information and comments."""
    boardgame = BoardGame.objects.get(id=boardgame_id)
    categories = boardgame.category.all()
    # altnames = boardgame.alternative_names["alternative_names"]
    comments = boardgame.comment_set.order_by("-date_added")
    context = {
        "boardgame": boardgame,
        "categories": categories,
        "comments": comments,
        # "altnames": altnames,
    }
    return render(request, "game_board/boardgame.html", context)


@login_required
def new_boardgame(request):
    """Add a new Board Game."""
    if request.method != "POST":
        # No data submitted; create a blank form.
        form = BoardGameForm()
    else:
        # POST data submitted; process data.
        form = BoardGameForm(data=request.POST)
        if form.is_valid():
            new_boardgame = form.save(commit=False)
            new_boardgame.owner = request.user.profile
            new_boardgame.save()
            form.save_m2m()
            return redirect("game_board:boardgames")

    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "game_board/new_boardgame.html", context)


@login_required
def edit_boardgame(request, boardgame_id):
    """Edit an existing Board Game."""
    boardgame = BoardGame.objects.get(id=boardgame_id)

    if request.method != "POST":
        form = BoardGameForm(instance=boardgame)
    else:
        form = BoardGameForm(instance=boardgame, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("game_board:boardgame", boardgame_id=boardgame_id)

    context = {"boardgame": boardgame, "form": form}
    return render(request, "game_board/edit_boardgame.html", context)


@login_required
def remove_boardgame(request, boardgame_id):
    """Remove an existing Board Game."""
    boardgame = BoardGame.objects.get(id=boardgame_id)

    if request.method != "POST":
        form = BoardGameForm(instance=boardgame)
    else:
        boardgame.delete()
        return redirect("game_board:boardgames")

    context = {"boardgame": boardgame, "form": form}
    return render(request, "game_board/remove_boardgame.html", context)


@login_required
def new_comment(request, boardgame_id):
    """Add a new comment for a particular Board Game."""
    boardgame = BoardGame.objects.get(id=boardgame_id)

    if request.method != "POST":
        # No data submitted; create a blank form
        form = CommentForm()
    else:
        # POST data submitted; process data.
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.owner = request.user.profile
            new_comment.board_game = BoardGame.objects.get(id=boardgame_id)
            new_comment.save()
            return redirect("game_board:boardgame", boardgame_id=boardgame_id)

    # Display a blank or invalid form.
    context = {"boardgame": boardgame, "form": form}
    return render(request, "game_board/new_comment.html", context)


@login_required
def edit_comment(request, comment_id):
    """Edit an existing comment."""
    comment = Comment.objects.get(id=comment_id)
    boardgame = comment.board_game

    if request.method != "POST":
        # Initial request; pre-fill form with the current comment.
        form = CommentForm(instance=comment)
    else:
        # POST data submitted; process data.
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("game_board:boardgame", boardgame_id=boardgame.id)
    context = {"comment": comment, "boardgame": boardgame, "form": form}
    return render(request, "game_board/edit_comment.html", context)


def categories(request):
    """Show all categories"""
    categories = Category.objects.order_by("name")
    context = {"categories": categories}
    return render(request, "game_board/categories.html", context)


def category(request, category_id):
    """Show a single category and all its related board games."""
    category = Category.objects.get(id=category_id)
    boardgames = category.boardgame_set.order_by("-date_added")
    context = {"category": category, "boardgames": boardgames}
    return render(request, "game_board/category.html", context)


@login_required
def profile(request):
    """Show profile of the Gamer."""
    profile = request.user.profile
    boardgames = profile.boardgame_set.all()
    lendout = LoanRecord.objects.filter(date_return=None)
    lendin = LoanRecord.objects.filter(date_return=None, debit=profile)
    context = {
        "profile": profile,
        "boardgames": boardgames,
        "lendout": lendout,
        "lendin": lendin,
    }
    return render(request, "game_board/profile.html", context)


@login_required
def update_profile(request):
    """Update the profile of Gamer."""
    profile = request.user.profile

    if request.method != "POST":
        # No data submitted; pre-fill form with the current gamer info
        form = ProfileForm(instance=profile)
    else:
        # POST data submitted; process data.
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            new_profile = form.save(commit=False)
            request.user.username = new_profile.username
            request.user.save()
            new_profile.save()
            return redirect("game_board:profile")
    context = {"profile": profile, "form": form}
    return render(request, "game_board/update_profile.html", context)


@login_required
def lend(request, boardgame_id):
    """lend board game"""
    boardgame = BoardGame.objects.get(id=boardgame_id)
    form = LoanRecordForm(
        request.POST or None,
        initial={"board_game": boardgame, "debit": request.user.profile},
    )
    if request.method == "POST":
        if request.user.profile.lend_limit_status >= 3:
            messages.error(
                request,
                "<h4><i class='bi bi-exclamation-octagon-fill'></i>&nbsp;Exceed Limitation!</h4>Your have lended more than or equal to 3 Board Games. Please return some of them back first. <hr />",
            )

        else:
            if form.is_valid():
                form.save()
                boardgame.available_status = False
                boardgame.save()
                request.user.profile.lend_limit_status += 1
                request.user.profile.save()
                return redirect("game_board:boardgames")
    context = {"boardgame": boardgame, "form": form}
    return render(request, "game_board/lend.html", context)


@login_required
def lendreturn(request, loanrecord_id):
    """Return the lended board game"""
    loanrecord = LoanRecord.objects.get(id=loanrecord_id)
    boardgame = loanrecord.board_game
    if request.method != "POST":
        form = LoanRecordForm(instance=loanrecord)
    else:
        form = LoanRecordForm(instance=loanrecord, data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.date_return = datetime.now()
            new_form.save()
            boardgame.available_status = True
            boardgame.save()
            request.user.profile.lend_limit_status -= 1
            request.user.profile.save()
            return redirect("game_board:profile")
    context = {"loanrecord": loanrecord, "boardgame": boardgame, "form": form}
    return render(request, "game_board/lendreturn.html", context)


def lendstatics(request):
    loanrecords = LoanRecord.objects.filter(date_return=None).order_by("board_game")
    context = {"loanrecords": loanrecords}
    return render(request, "game_board/lendstatics.html", context)


def lendhistory(request, boardgame_id):
    boardgame = BoardGame.objects.get(id=boardgame_id)
    loanrecords = LoanRecord.objects.filter(board_game=boardgame).order_by(
        "-date_lended"
    )
    context = {"boardgame": boardgame, "loanrecords": loanrecords}
    return render(request, "game_board/lendhistory.html", context)


def custom_404(request, exception):
    return render(request, "custom_404.html")
