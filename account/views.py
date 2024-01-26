from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import secrets
from rest_framework_simplejwt.tokens import RefreshToken
from .models import MyUser
from .serializer import (
    TokenSerializer,
    EmailPostSerializer,
    EmailPasswordSerializer
    )
from .mail import send_email
from django.contrib.auth import authenticate


def get_tokens_for_user(user, **kwargs):
    refresh = RefreshToken.for_user(user)

    access_token = TokenSerializer.get_token(user, **kwargs)

    return {
        "refresh": str(refresh),
        "access": str(access_token.access_token),
    }

def makePassword():
    password_length = 5 
    password = secrets.token_urlsafe(password_length)
    unique_number = secrets.randbelow(1000)
    password += str(unique_number)
    return password


class Register(APIView):
    def post(self, request):
        try:
            serializer = EmailPostSerializer(data=request.data)
            if serializer.is_valid():
                email = serializer.validated_data.get('email')
                
                # Check if the user already exists
                if MyUser.objects.filter(email=email).exists():
                    return Response({'msg': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)

                password = makePassword()
                MyUser.objects.create(email=email, password=password)
                print('hello')
                send_email(password=password, email=email)
                return Response({'msg': f'Password sent to your email${password}'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'msg': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self,request):
        try:
            serializer = EmailPasswordSerializer(data=request.data)
            if serializer.is_valid():
                email = serializer.validated_data.get('email')
                if MyUser.objects.filter(email=email).exists():
                    password = serializer.validated_data.get('password')
                    print(email,password)
                    authenticate(request,email=email,password=password)
                    user = MyUser.objects.get(email=email)
                    token = get_tokens_for_user(user)
                    return Response(token,status=status.HTTP_200_OK)
                return Response({'msg':'Email Does not exist'},status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'msg':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)


class ForgotPassword(APIView):
    def post(self,request):
        try:
            email = request.data.get('email')
            MyUser.objects.get(email=email)
        except Exception as e:
            return Response({'msg':'this email id does not have an account'},status=status.HTTP_400_BAD_REQUEST)
        password = makePassword()
        user = MyUser.objects.get(email=email)
        user.set_password(password)
        user.save()
        send_email(password=password,email=email)
        return Response({'msg':'new pass word send to your email'},status=status.HTTP_200_OK)
        


# Create your views here.
