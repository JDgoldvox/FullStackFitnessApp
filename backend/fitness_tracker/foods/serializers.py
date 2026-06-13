from .models import Food
from rest_framework import serializers

class FoodSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    class Meta:
        model=Food
        fields = ["owner", "day", "calories"]
