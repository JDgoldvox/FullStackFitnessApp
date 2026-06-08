from django.contrib.auth.models import Group, User
from rest_framework import serializers
from steps.views import StepCount
from restapi.models import Workout, WORKOUT_TYPES


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]

class StepCountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StepCount
        fields = ["steps", "goal", "day"]


class WorkoutSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    class Meta:
        model = Workout
        fields = ["owner", "time", "name", "type", "duration"]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    workouts = serializers.HyperlinkedRelatedField(
        many=True, view_name="workout-detail", read_only=True)

    class Meta:
        model = User
        fields = ["url", "id", "username", "workouts"]
