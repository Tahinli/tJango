from rest_framework import serializers
from .models import UserToken


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToken
        fields = "__all__"
        read_only_fields = ["user", "token"]
