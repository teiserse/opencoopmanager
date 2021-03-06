# Generated by Django 3.0.6 on 2020-06-03 15:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opencoopmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='elligible_voters',
            field=models.ManyToManyField(default=[1], related_name='can_vote_in', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vote',
            name='remaining_voters',
            field=models.ManyToManyField(default=[1], related_name='not_voted_in', to=settings.AUTH_USER_MODEL),
        ),
    ]
