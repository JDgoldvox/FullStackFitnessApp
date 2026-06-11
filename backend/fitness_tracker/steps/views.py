from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import StepCount
from rest_framework import viewsets, permissions
from .serializers import StepCountSerializer


class StepsViewSet(viewsets.ModelViewSet):
    # queryset = StepCount.objects.all().order_by("day")
    serializer_class = StepCountSerializer
    permission_classes = [permissions.DjangoObjectPermissions]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return StepCount.objects.filter(owner=self.request.user).order_by("day")

