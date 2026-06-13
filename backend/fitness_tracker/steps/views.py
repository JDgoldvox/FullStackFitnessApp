from .models import StepCount, StepGoal
from .serializers import StepCountSerializer, StepGoalSerializer
from restapi.permissions import IsAdminOrSelf
from django.contrib.auth.models import User

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action


class StepsViewSet(viewsets.ModelViewSet):
    queryset = StepCount.objects.all().order_by("day")
    serializer_class = StepCountSerializer
    permission_classes = [permissions.DjangoObjectPermissions]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
class StepGoalViewSet(viewsets.ModelViewSet):
    queryset = StepGoal.objects.all()
    serializer_class = StepGoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    @action(methods=['get'], detail=True, permission_classes=[IsAdminOrSelf],
            url_path="count", url_name="count_step_goals")
    def count_passes(self, request, pk):
        goal = StepGoal.objects.get(id=pk).goal # only works if step goal order is same order as users
        return Response({
            "steps": StepCount.objects.filter(steps__gte=goal).count(),
            "goal": goal,
        })

