from django.contrib.auth.models import Group, User
from .permissions import IsOwnerOrReadOnly

from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .serializers import GroupSerializer, UserSerializer, StepCountSerializer
from steps.views import StepCount

from rest_framework import generics
from .models import Workout
from .serializers import WorkoutSerializer

# @api_view(["GET"])
# def api_root(request, format=None):
#     return Response({
#         "users": reverse("user-list", request=request, format=format),
#         "snippets": reverse("workout-list", request=request, format=format)
#     })

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# class WorkoutList(generics.ListCreateAPIView):
#     """
#     List all workouts, or create a new workout.
#     """

#     queryset = Workout.objects.all()
#     serializer_class = WorkoutSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class WorkoutDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     Retrieve, update or delete a workout instance.
#     """

#     queryset = Workout.objects.all()
#     serializer_class = WorkoutSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class StepsViewSet(viewsets.ModelViewSet):
    queryset = StepCount.objects.all().order_by("day")
    serializer_class = StepCountSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]


