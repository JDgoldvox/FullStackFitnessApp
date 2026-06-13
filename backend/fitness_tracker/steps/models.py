import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class StepGoal(models.Model):
    # owner = models.ForeignKey(User, related_name="step_goal", on_delete=models.CASCADE, unique=True)
    owner = models.OneToOneField(User, related_name="step_goal", on_delete=models.CASCADE)
    goal = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.owner.username}: {self.goal}"
    
    class Meta:
        ordering = ["owner"]

class StepCount(models.Model):
    owner = models.ForeignKey(User, related_name="steps", on_delete=models.CASCADE, null=True)
    # goal = models.IntegerField(default=0)
    steps = models.IntegerField(default=0)
    day = models.DateField("day", default=timezone.now)

    def __str__(self):
        return f"{self.owner.username}({self.day}): {self.has_reached_goal()}" # type: ignore
    
    def has_reached_goal(self) -> bool:
        return self.steps >= StepGoal.objects.get(id=self.owner.id).goal # type: ignore
    
    class Meta:
        ordering = ["day", "owner"]
        constraints = [
            models.UniqueConstraint(
                fields = ['owner', 'day'],
                name = "unique_owner_steps_day"
            )
        ]