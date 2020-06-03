from django.contrib import admin

from django.contrib.auth.models import User
from .models import Vote, VoteChoice

class VoteChoiceInline(admin.StackedInline):
    model = VoteChoice
    extra = 2

class VoteAdmin(admin.ModelAdmin):
    inlines = [VoteChoiceInline]
    fields = ('title','description','start_date','end_date','elligible_voters')

    def save_model(self, request, obj, form, change):
        obj.save()
        if not change:
            for pk in request.POST['elligible_voters']:
                obj.remaining_voters.add(User.objects.get(id=int(pk)))
        super().save_model(request, obj, form, change)

admin.site.register(Vote, VoteAdmin)
