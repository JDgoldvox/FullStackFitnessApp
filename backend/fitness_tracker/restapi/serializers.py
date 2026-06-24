from django.contrib.auth.models import Group, User
from rest_framework import serializers

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    goals = serializers.HyperlinkedRelatedField(
        many=False, view_name="all_goals-detail", read_only=True)
    workouts = serializers.HyperlinkedRelatedField(
        many=True, view_name="workouts-detail", read_only=True)
    steps = serializers.HyperlinkedRelatedField(
        many=True, view_name="steps-detail", read_only=True)
    foods = serializers.HyperlinkedRelatedField(
        many=True, view_name="foods-detail", read_only=True)
    

    class Meta:
        model = User
        fields = ["url", "id", "username", "all_goals"] # "workouts", "steps", "foods"
