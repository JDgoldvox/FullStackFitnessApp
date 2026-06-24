from django.db import models
from django.contrib.auth.models import User


class UserGoals(models.Model):
    owner = models.OneToOneField(User, related_name="all_goals", on_delete=models.CASCADE)
    # water goal
    # heart rate goal

    def __str__(self) -> str:
        return f"Goals for {self.owner.username}"

    class Meta:
        ordering = ["owner"]

