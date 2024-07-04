from rest_framework.viewsets import ReadOnlyModelViewSet
from tJango import permissions as tJango_permissions
from .models import UserToken
from .serializers import UserTokenSerializer


class UserTokenViewSet(ReadOnlyModelViewSet):
    queryset = UserToken.objects.all()
    serializer_class = UserTokenSerializer
    permission_classes = [tJango_permissions.IsOwnerOrIsAdminOrHasToken]
