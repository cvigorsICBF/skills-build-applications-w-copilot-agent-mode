from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='dc', description='DC Superheroes')

        # Create users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel.name)
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel.name)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc.name)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc.name)

        # Create workouts
        pushups = Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='marvel')
        squats = Workout.objects.create(name='Squats', description='Do 30 squats', suggested_for='dc')

        # Create activities
        Activity.objects.create(user=ironman, type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=batman, type='cycle', duration=45, date=timezone.now().date())

        # Create leaderboard
        Leaderboard.objects.create(user=ironman, score=100, rank=1)
        Leaderboard.objects.create(user=batman, score=90, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
