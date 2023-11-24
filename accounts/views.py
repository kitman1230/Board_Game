from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from game_board.models import Profile
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    """Register a new user."""
    if request.method != "POST":
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            profile = Profile.objects.create(
                user=request.user, username=request.user.username
            )
            profile.save()
            return redirect("game_board:profile")

    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "registration/register.html", context)
