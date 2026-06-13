from rest_framework import serializers
from .models import Workout

class WorkoutSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    class Meta:
        model = Workout
        fields = ["owner", "time", "name", "type", "duration"]