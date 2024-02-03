from django.contrib.auth import authenticate
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import uuid
import time
from .models import (
    GroupMessage,
    GlobalGroup,
    BlockedUser,
    Search
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




@permission_classes([IsAuthenticated])
class GetGlobalGrroups(APIView):
    def get(self,request):
        groups = GlobalGroup.objects.all()
        serializer = GlobalGroupSerializer(groups,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)




class SearchRandomPerson(APIView):
    def get(self, request):
        user = request.user

        search, created = Search.objects.get_or_create(user=user)

        search.is_searching = True
        search.save()

        time.sleep(1)

        random_person = Search.objects.filter(is_searching=True).exclude(user=user).first()

        if random_person:
            chat_id = str(uuid.uuid4())
            search.is_searching = False
            search.save()
            random_person.is_searching = False
            random_person.save()

            return Response({'chat_id': chat_id}, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'No one online'}, status=status.HTTP_200_OK)


# Create your views here.
