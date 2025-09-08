from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models

# Sample models for demonstration (should be replaced with actual models)
from octofit_tracker import models as octofit_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        octofit_models.User.objects.all().delete()
        octofit_models.Team.objects.all().delete()
        octofit_models.Activity.objects.all().delete()
        octofit_models.Leaderboard.objects.all().delete()
        octofit_models.Workout.objects.all().delete()

        # Create teams
        marvel = octofit_models.Team.objects.create(name='Marvel')
        dc = octofit_models.Team.objects.create(name='DC')

        # Create users (super heroes)
        users = [
            octofit_models.User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            octofit_models.User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            octofit_models.User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            octofit_models.User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        # Create activities
        activities = [
            octofit_models.Activity.objects.create(user=users[0], type='Running', duration=30),
            octofit_models.Activity.objects.create(user=users[1], type='Cycling', duration=45),
            octofit_models.Activity.objects.create(user=users[2], type='Swimming', duration=25),
            octofit_models.Activity.objects.create(user=users[3], type='Yoga', duration=60),
        ]

        # Create workouts
        workouts = [
            octofit_models.Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout'),
            octofit_models.Workout.objects.create(name='Strength Training', description='Build muscle strength'),
        ]

        # Create leaderboard
        octofit_models.Leaderboard.objects.create(team=marvel, points=100)
        octofit_models.Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
