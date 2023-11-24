from django.contrib import admin
from .models import Profile, BoardGame, Category, Comment, LoanRecord

# Register your models here.
admin.site.register(Profile)
admin.site.register(BoardGame)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(LoanRecord)
