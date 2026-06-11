from rest_framework import serializers
from steps.views import StepCount

class StepCountSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    class Meta:
        model = StepCount
        fields = ["owner", "steps", "goal", "day"]