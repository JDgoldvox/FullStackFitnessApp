from django.contrib.auth.models import Group, User
from .permissions import IsOwnerOrReadOnly, IsAdminOrSelf

from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import GroupSerializer, UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    @action(methods=['get'], detail=False, permission_classes=[IsAdminOrSelf],
            url_path="current-user", url_name="current_user")
    def get_current_user(self, request):
        resp = UserSerializer(
            User.objects.get(id=request.user.id),
            context={"request": request}
        )
        return Response(resp.data)
