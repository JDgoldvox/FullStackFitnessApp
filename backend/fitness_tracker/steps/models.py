import datetime
from django.db import models
from django.utils import timezone

class StepCount(models.Model):
    owner = models.ForeignKey("auth.User", related_name="steps", on_delete=models.CASCADE, null=True)
    goal = models.IntegerField(default=0)
    steps = models.IntegerField(default=0)
    day = models.DateField("day", default=timezone.now())

    def __str__(self):
        return f"{self.day}: {self.has_reached_goal()}"
    
    def has_reached_goal(self):
        return self.steps >= self.goal
    
    class Meta:
        ordering = ["day"]
        constraints = [
            models.UniqueConstraint(
                fields = ['owner', 'day', 'steps'],
                name = "unique_owner_steps_day"
            )
        ]