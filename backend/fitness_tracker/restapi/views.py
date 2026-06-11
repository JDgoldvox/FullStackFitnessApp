from django.contrib.auth.models import Group, User
from .permissions import IsOwnerOrReadOnly, IsSelf

from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import GroupSerializer, UserSerializer, WorkoutSerializer

from rest_framework import generics
from .models import Workout

class WorkoutViewSet(viewsets.ModelViewSet):
    # queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Workout.objects.filter(owner=self.request.user).order_by("time", "duration")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    @action(methods=['get'], detail=False, permission_classes=[IsSelf],
            url_path="current-user", url_name="current_user")
    def get_current_user(self, request):
        resp = UserSerializer(
            User.objects.get(id=request.user.id),
            context={"request": request}
        )
        return Response(resp.data)
