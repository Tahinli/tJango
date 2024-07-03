from rest_framework.viewsets import ReadOnlyModelViewSet

# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import UserToken
from .serializers import UserTokenSerializer


class UserViewSet(ReadOnlyModelViewSet):
    queryset = UserToken.objects.all()
    serializer_class = UserTokenSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
