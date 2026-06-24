from .models import UserGoals
from rest_framework import serializers

class UserGoalSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = UserGoals
        ordering = ["owner"]