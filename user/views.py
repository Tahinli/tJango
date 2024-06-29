from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import User
from .serializers import UserSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def print_this(self, request, pk=None):
        print(self.get_object())
