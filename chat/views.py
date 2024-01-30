from django.contrib.auth import authenticate
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import (
    GroupMessage,
    GlobalGroup,
    BlockedUser
)
from .serializer import (
    GlobalGroupSerializer,
    GlobalGroupPostSerializer
)


@permission_classes([IsAuthenticated])
class ManageGlobalGroup(APIView):
    def post(self,request):
        admin = request.user
        existing_group = GlobalGroup.objects.filter(group_admin=admin)
        if not existing_group.exists():
            serializer = GlobalGroupPostSerializer(data=request.data)
            if serializer.is_valid():
                name = serializer.validated_data.get('name')
                subject = serializer.validated_data.get('subject')
                group = GlobalGroup.objects.create(
                    group_admin=admin,
                    name=name,
                    subject=subject
                )
                group.members.add(request.user)
                serializer = GlobalGroupSerializer(group)
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        serializer = GlobalGroupSerializer(existing_group[0])
        return Response({'msg':'already an admin','group':serializer.data},status=status.HTTP_400_BAD_REQUEST)








# Create your views here.
