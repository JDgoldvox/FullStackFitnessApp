from django.db import models

WORKOUT_TYPES = [("running", "running"), ("walking", "walking"), ("cycling", "cycling"), ("sit-up", "sit-up"), ("bench press", "bench press")]

class Workout(models.Model):
    owner = models.ForeignKey("auth.User", related_name="workouts", on_delete=models.CASCADE)
    time = models.DateTimeField()
    name = models.CharField(max_length=200, unique=True)
    type = models.CharField(choices=WORKOUT_TYPES)
    duration = models.DurationField()

    def __str__(self):
        return f"{self.owner}: {self.name}"

    class Meta:
        ordering = ["time", "type", "duration"]
        constraints = [
            models.UniqueConstraint(
                fields = ['owner', 'name'],
                name = "unq_ownr_wkt_name"
            )
        ]


