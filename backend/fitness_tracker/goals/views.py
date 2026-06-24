from .models import UserGoals
from .serializers import UserGoalSerializer

from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from restapi.permissions import IsOwnerOrReadOnly, IsAdminOrSelf

class UserGoalViewSet(viewsets.ModelViewSet):
    queryset = UserGoals.objects.all()
    serializer_class = UserGoalSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action == "retrieve":
            permission_classes = [IsAdminOrSelf]
        else:
            permission_classes = [permissions.IsAdminUser]

        return [permissions() for permissions in permission_classes]
