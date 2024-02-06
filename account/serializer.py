from rest_framework import serializers
from .models import MyUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class TokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user, **kwargs):
        token = super().get_token(user)
        if user.email:
            token["email"] = user.email
        if user.username:
            token["username"] = user.username

        return token
    
class EmailPostSerializer(serializers.Serializer):
    email = serializers.EmailField()

class PasswordPostSerializer(serializers.Serializer):
    newpassword = serializers.CharField()

class EmailPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)

class MyuserUsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ["id", "username"]