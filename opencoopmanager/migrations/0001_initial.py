# Generated by Django 3.0.4 on 2020-03-15 13:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=2500)),
                ('start_date', models.DateTimeField(verbose_name='Voting Starts')),
                ('end_date', models.DateTimeField(verbose_name='Voting Ends')),
            ],
        ),
        migrations.CreateModel(
            name='VoteChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveIntegerField()),
                ('choice_text', models.CharField(max_length=250)),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opencoopmanager.Vote')),
            ],
        ),
        migrations.CreateModel(
            name='Ballot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choices', models.CharField(max_length=250, validators=[django.core.validators.int_list_validator])),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opencoopmanager.Vote')),
            ],
        ),
    ]
