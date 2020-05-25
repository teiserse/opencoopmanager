from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Vote, VoteChoice, Ballot

@login_required
def index(request):
    vote_list = Vote.objects.order_by('start_date')
    context = {'vote_list': vote_list}
    return render(request, 'opencoopmanager/index.html', context)

@login_required
def votemain(request, vote_id):
    vote = get_object_or_404(Vote, pk=vote_id)
    return render(request, 'opencoopmanager/votemain.html', {'vote': vote})

@login_required
def sendballot(request, vote_id):
    vote = get_object_or_404(Vote, pk=vote_id)
    ballot = {}
    for choice in vote.votechoice_set.all():
        try:
            preference = request.POST[str(choice.index)]
        except (KeyError):
            pass
        else:
            ballot[int(preference)] = choice.index

    for pref in range(1, len(ballot) + 1):
        try:
            test = ballot[pref]
        except (KeyError):
            return render(request, 'opencoopmanager/votemain.html',{
                'vote': vote,
                'error_message': ("Selections have to be made by numbers from"
                " 1 upwards, with no spaces up to your final choice.")
            })
        else:
            pass

    Ballot.create(vote, ballot).save()
    return HttpResponseRedirect(reverse('opencoopmanager:index'))
