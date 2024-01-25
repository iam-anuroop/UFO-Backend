from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Register(APIView):
    def post(self,request):
        email = request.data.get('email')
        return Response({'msg':'otp sent successfully'},status=status.HTTP_200_OK)


class OtpVerify(APIView):
    def post(self,request):
        otp = request.data.get('otp')
        return Response({'msg':'otp verified'},status=status.HTTP_200_OK)



# Create your views here.
