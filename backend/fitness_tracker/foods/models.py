from django.db import models
from django.utils import timezone

from goals.views import UserGoals


class Food(models.Model):
    owner = models.ForeignKey("auth.User", related_name="foods", on_delete=models.CASCADE)
    day = models.DateField(default=timezone.now)
    calories = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.owner.username} ({self.day}): {self.calories}"
    
    class Meta:
        ordering = ["owner", "day"]

class FoodGoal(models.Model):
    owner = models.OneToOneField(UserGoals, related_name="food_goal", on_delete=models.CASCADE)
    goal = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.owner.owner.username}: {self.goal}"
    
    class Meta:
        ordering = ["owner"]
