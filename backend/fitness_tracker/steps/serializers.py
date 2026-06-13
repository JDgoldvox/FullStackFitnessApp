from rest_framework import serializers
from .views import StepCount, StepGoal

class StepCountSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    class Meta:
        model = StepCount
        fields = ["owner", "steps", "day"]

class StepGoalSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    class Meta:
        model=StepGoal
        fields=["owner", "goal"]