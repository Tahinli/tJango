from rest_framework import serializers
from .models import User
from user_token.serializers import UserTokenSerializer


class UserSerializer(serializers.ModelSerializer):
    tokens = UserTokenSerializer(many=True)

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ["date_created", "tokens"]
