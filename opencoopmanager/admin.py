from django.contrib import admin

from .models import Vote, VoteChoice

class VoteChoiceInline(admin.StackedInline):
    model = VoteChoice
    extra = 2

class VoteAdmin(admin.ModelAdmin):
    inlines = [VoteChoiceInline]

admin.site.register(Vote, VoteAdmin)
