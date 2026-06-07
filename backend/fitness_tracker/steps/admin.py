from django.contrib import admin

from .models import Question, StepCount

admin.site.register(Question)
admin.site.register(StepCount)