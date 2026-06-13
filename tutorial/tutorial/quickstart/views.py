from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets


from tutorial.quickstart.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    This is the API viewpoint that allows users to be edited or viewed
    """
    queryset = User.objects.all().order_by("-date-joined")
    serializer_class = UserSerializer
    permission_classes = [permission.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    This is the API viewpoint that allows groups to be edited or viewed
    """
    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permission.IsAuthenticated]
