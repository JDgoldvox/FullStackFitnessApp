from django.utils import timezone
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from enum import Enum
import operator
from functools import reduce

from goals.views import UserGoals

class WorkoutType(models.TextChoices):
    RUN = 'RN', _('running')
    WALK = 'WK', _('walking')
    CYCLE = "CY", _("cycling")
    SIT_UP = "SU", _("sit-up")
    BENCH_PRESS = "BP", _("bench-press")
    SQUAT = 'SQ', _('squat')
    DEADLIFT = 'DL', _('deadlift')

class MetricType(models.TextChoices):
    REPS = 'REPS', _("repitions")
    WEIGHT_LBS = 'LBS', _("Pounds")
    WEIGHT_KGS = 'KG', _("kilograms")
    TIME_MIN = "MIN", _("minutes")
    TIME_HR = "HR", _("hours")
    DISTANCE_MI = "MI", _("miles")
    DISTANCE_KM = "KM", _("kilometers")

class WorkoutCategories:
    def __init__(self) -> None:
        raise TypeError("This class cannot be instantiated.")

    class MetricCategories():
        COUNT = [MetricType.REPS]
        TIME = [MetricType.TIME_MIN, MetricType.TIME_HR]
        WEIGHT = [MetricType.WEIGHT_KGS, MetricType.WEIGHT_LBS]
        DISTANCE = [MetricType.DISTANCE_KM, MetricType.DISTANCE_MI]

    class WkType(Enum):
        CARDIO = 0
        LIFTING = 1
        BODYWEIGHT = 2

    CATEGORIES = {
        WkType.CARDIO: {
            'workouts': [WorkoutType.RUN, WorkoutType.WALK],
            'metrics': [MetricCategories.DISTANCE, MetricCategories.TIME],
        },
        WkType.LIFTING: {
            'workouts': [WorkoutType.SQUAT, WorkoutType.BENCH_PRESS, WorkoutType.DEADLIFT],
            'metrics': [MetricCategories.COUNT, MetricCategories.WEIGHT],
        },
        WkType.BODYWEIGHT: {
            'workouts': [WorkoutType.SIT_UP],
            'metrics': [MetricCategories.COUNT]
        }
    }

    @classmethod
    def get_allowed_metrics(cls, workout_type):
        for wkCat in cls.CATEGORIES.values():
            if workout_type in wkCat['workouts']:
                return wkCat['metrics']
        return []

class Workout(models.Model):
    owner = models.ForeignKey("auth.User", related_name="workouts", on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now, help_text="date/time workout started")
    name = models.CharField(max_length=200, unique=True, help_text="Name of workout")
    type = models.CharField(choices=WorkoutType.choices, help_text="workout type")
    metric = models.CharField(
        choices=MetricType.choices,
        help_text="Measuring Type"
    )
    duration = models.DurationField()

    def clean(self) -> None:
        super().clean()
        
        allowed_metrics = WorkoutCategories.get_allowed_metrics(self.type)
        if self.metric not in allowed_metrics:
            raise ValidationError({
                'metric': f"Invlalid combination. You cannot measure {self.type} in {self.metric}"
            })

    def __str__(self):
        return f"{self.owner}: {self.name}"

    class Meta:
        ordering = ["time", "type", "duration"]
        constraints = [
            models.UniqueConstraint(
                fields = ['owner', 'name'],
                name = "unq_ownr_wkt_name"
            ),
            models.CheckConstraint(
                condition=(
                    reduce(
                        operator.or_,
                        [
                            models.Q(
                                type__in=category['workouts'],
                                metric__in=category['metrics']
                            )
                            for category in WorkoutCategories.CATEGORIES.values()
                        ]
                    )
                ),
                name="valid_workout_metric_combo"
            )
        ]


class WorkoutGoal(models.Model):
    owner = models.OneToOneField(UserGoals, related_name="workout_goal", on_delete=models.CASCADE)
    type = models.CharField(
        choices=WorkoutType.choices,
        help_text="workout type"
    )
    metric = models.CharField(
        choices=MetricType.choices,
        help_text="measuring type"
    )
    goal = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.owner.owner.username}: {self.type} - {self.goal}"
    
    class Meta:
        ordering = ["owner"]
        constraints = [
            models.CheckConstraint(
                condition=reduce(
                    operator.or_,
                        [
                            models.Q(
                                type__in=category['workouts'],
                                metric__in=category['metrics']
                            )
                            for category in WorkoutCategories.CATEGORIES.values()
                        ]
                ),
                name="valid_workout_metric_combo_goal"
            )
        ]
