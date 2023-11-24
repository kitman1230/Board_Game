from django.db import models
from django.contrib.auth.models import User

# from django.utils import timezone


# Create your models here.
class Profile(models.Model):
    """name, birthday, gender, lended boardgame(multi)"""

    class Lend_Limit(models.IntegerChoices):
        Zero = 0
        One = 1
        Two = 2
        Three = 3

    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, blank=True)
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    birthday = models.DateField(blank=True, null=True)
    lend_limit_status = models.PositiveSmallIntegerField(
        choices=Lend_Limit.choices, default=Lend_Limit.Zero
    )

    def __str__(self):
        """Return a string representation of the profile"""
        return self.username


class Category(models.Model):
    """Categories of the Board Game. Only admin can edit it"""

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name

    class Meta:
        ordering = ["name"]


class BoardGame(models.Model):
    """Board game information"""

    class Complexity_Rating(models.IntegerChoices):
        One = 1
        Two = 2
        Three = 3
        Four = 4
        Five = 5

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    last_edit_date = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    publish_year = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(max_length=2000, blank=True, null=True)
    min_players = models.PositiveSmallIntegerField()
    max_players = models.PositiveSmallIntegerField(blank=True, null=True)
    min_time_period = models.PositiveSmallIntegerField()
    max_time_period = models.PositiveSmallIntegerField(blank=True, null=True)
    age_limit = models.PositiveSmallIntegerField(default=3)
    complexity_rating = models.PositiveSmallIntegerField(
        choices=Complexity_Rating.choices, default=Complexity_Rating.One
    )
    available_status = models.BooleanField(default=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class Comment(models.Model):
    """Comment on BoardGame"""

    class Rate(models.IntegerChoices):
        BAD = 1
        SOSO = 2
        NORMAL = 3
        GOOD = 4
        EXCELLENT = 5

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    board_game = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=Rate.choices)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    last_edit_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a simple string representing the comment."""
        return f"{self.text[:50]}..."


class LoanRecord(models.Model):
    """Record all the status of the lending"""

    board_game = models.ForeignKey(BoardGame, on_delete=models.DO_NOTHING)
    debit = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    date_lended = models.DateTimeField(auto_now_add=True)
    date_return = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        """Return the game name to represent the record"""
        return self.board_game.name
