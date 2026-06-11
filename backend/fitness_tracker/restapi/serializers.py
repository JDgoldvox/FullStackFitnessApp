from django.contrib.auth.models import Group, User
from rest_framework import serializers
from restapi.models import Workout


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]

class WorkoutSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    class Meta:
        model = Workout
        fields = ["owner", "time", "name", "type", "duration"]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    workouts = serializers.HyperlinkedRelatedField(
        many=True, view_name="workout-detail", read_only=True)
    steps = serializers.HyperlinkedRelatedField(
        many=True, view_name="steps-detail", read_only=True)

    class Meta:
        model = User
        fields = ["url", "id", "username", "workouts", "steps"]
