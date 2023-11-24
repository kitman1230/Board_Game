from django import forms
from .models import BoardGame, Comment, Profile, LoanRecord, Category


class BoardGameForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all().order_by("name"),
        widget=forms.CheckboxSelectMultiple,
    )

    # category = forms.MultipleChoiceField(
    #    widget=forms.CheckboxSelectMultiple,
    #    choices=[
    #        ("", "All"),
    #    ]
    #    + [(category.id, category) for category in Category.objects.all()],
    # )

    # def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #
    #    categories = Category.objects.all().order_by("name")
    #    CATEGORY_CHOICES = ()
    #    for category in categories:
    #        CATEGORY_CHOICES += ((category.id, category),)
    #
    #    self.fields["category"] = forms.MultipleChoiceField(
    #        choices=CATEGORY_CHOICES, widget=forms.CheckboxSelectMultiple
    #    )

    # self.fields["category"].widget.attrs.update({"class": "special"})
    # self.fields["category"] = forms.Select(
    #    # choices=CATEGORY_CHOICES,
    # )

    class Meta:
        model = BoardGame
        exclude = ("owner", "available_status")
        # widget = {"category": forms.MultipleChoiceField(choices=CATEGORY_CHOICES)}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ("owner", "board_game")
        labels = {
            "rating": "Rate",
            "text": "Comment",
        }


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].disabled = True

    class Meta:
        model = Profile
        fields = [
            "username",
            "firstname",
            "lastname",
            "birthday",
            "bio",
        ]
        labels = {
            "username": "Username",
            "firstname": "First / Given Name",
            "lastname": "Last / Family Name",
            "birthday": "Birthday",
            "bio": "Bio",
        }


class LoanRecordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["board_game"].disabled = True
        self.fields["debit"].disabled = True
        del self.fields["date_return"]

    class Meta:
        model = LoanRecord
        fields = "__all__"
        widgets = {
            "board_game": forms.Select(attrs={}),
            "debit": forms.Select(attrs={}),
        }
        labels = {
            "board_game": "Board Game",
            "debit": "Lended by",
        }
