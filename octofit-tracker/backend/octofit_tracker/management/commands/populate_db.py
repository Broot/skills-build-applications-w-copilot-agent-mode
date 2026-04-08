from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models


from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', team=marvel)
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='pass', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='pass', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='pass', team=dc)

        # Activities
        Activity.objects.create(user=ironman, type='run', duration=30, calories=300)
        Activity.objects.create(user=captain, type='cycle', duration=45, calories=400)
        Activity.objects.create(user=batman, type='swim', duration=60, calories=500)
        Activity.objects.create(user=superman, type='run', duration=50, calories=600)

        # Workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity for heroes', suggested_for=marvel)
        Workout.objects.create(name='Power Circuit', description='Strength for DC', suggested_for=dc)

        # Leaderboard
        Leaderboard.objects.create(user=ironman, score=300)
        Leaderboard.objects.create(user=captain, score=400)
        Leaderboard.objects.create(user=batman, score=500)
        Leaderboard.objects.create(user=superman, score=600)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))

# Models for reference (should be in octofit_tracker/models.py):
# class Team(models.Model):
#     name = models.CharField(max_length=100)
# class Activity(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     type = models.CharField(max_length=50)
#     duration = models.IntegerField()
#     calories = models.IntegerField()
# class Workout(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     suggested_for = models.ForeignKey(Team, on_delete=models.CASCADE)
# class Leaderboard(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     score = models.IntegerField()
