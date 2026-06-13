from .models import Workout
from .serializers import WorkoutSerializer

from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from restapi.permissions import IsOwnerOrReadOnly



class WorkoutViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self): # type: ignore
        return Workout.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(methods=['get'], detail=False, permission_classes=[permissions.IsAdminUser],
            url_path="all", url_name="get_all_workouts")
    def get_all(self, request):
        response = WorkoutSerializer(
            Workout.objects.all(),
            many=True,
            context={"request": request},
        )
        return Response(response.data)
