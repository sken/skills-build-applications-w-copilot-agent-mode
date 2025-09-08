
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Activity, User, Team, Workout, Leaderboard
from bson import ObjectId

def convert_objectid(data):
    def fix(obj):
        return {k: str(v) if isinstance(v, ObjectId) else v for k, v in obj.items()}
    return [fix(item) for item in data]

@api_view(['GET'])
def activities_list(request):
    activities = Activity.objects.all().values()
    return Response(convert_objectid(list(activities)))

@api_view(['GET'])
def users_list(request):
    users = User.objects.all().values()
    return Response(convert_objectid(list(users)))

@api_view(['GET'])
def teams_list(request):
    teams = Team.objects.all().values()
    return Response(convert_objectid(list(teams)))

@api_view(['GET'])
def workouts_list(request):
    workouts = Workout.objects.all().values()
    return Response(convert_objectid(list(workouts)))

@api_view(['GET'])
def leaderboard_list(request):
    leaderboard = Leaderboard.objects.all().values()
    return Response(convert_objectid(list(leaderboard)))
