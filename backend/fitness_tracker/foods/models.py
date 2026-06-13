from django.db import models
from django.utils import timezone


class Food(models.Model):
    owner = models.ForeignKey("auth.User", related_name="foods", on_delete=models.CASCADE)
    day = models.DateField(default=timezone.now)
    calories = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.owner.username} ({self.day}): {self.calories}"
    
    class Meta:
        ordering = ["owner", "day"]
