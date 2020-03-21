from django.db import models
from django.core.validators import int_list_validator

class Vote(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=2500)
    start_date = models.DateTimeField('Voting Starts')
    end_date = models.DateTimeField('Voting Ends')

    def __str__(self):
        return self.title

class VoteChoice(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    index = models.PositiveIntegerField()
    choice_text = models.CharField(max_length=250)

    def __str__(self):
        return self.vote.title + " - " + self.choice_text

class Ballot(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    choices = models.CharField(validators=[int_list_validator], max_length=250)

    def __str__(self):
        return self.vote.title + " - Ballot"

    """
    This method creates a new Ballot from the ballot being defined as a dict:
        ballot[preference] = index of vote choice
    """
    @classmethod
    def create(cls, vote, ballot):
        selection = ""
        for pref in range(1, vote.votechoice_set.count() + 1):
            selection = selection + str(ballot[pref])
            if not pref == vote.votechoice_set.count():
                selection = selection + ","
        return cls(vote=vote, choices=selection)
