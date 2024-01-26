from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class TokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user, **kwargs):
        token = super().get_token(user)
        if user.email:
            token["email"] = user.email
        return token
    
class EmailPostSerializer(serializers.Serializer):
    email = serializers.EmailField()

class EmailPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)