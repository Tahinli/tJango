from rest_framework import serializers
from .models import User, Token


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'
        read_only_fields = ['username', 'token']

class UserSerializer(serializers.ModelSerializer):
    token = TokenSerializer(read_only=True)
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['date_created']

    def token(self, object):
        print("İMDAAAAAAAAAAAAAAAAAAAAAAAAAAT")
        print(object.username)