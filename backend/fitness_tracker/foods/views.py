from .models import Food
from .serializers import FoodSerializer
from rest_framework import permissions, viewsets
from restapi.permissions import IsOwner

class FoodViewSet(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    permission_classes = [IsOwner]

    def get_queryset(self): # type: ignore
        return Food.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)