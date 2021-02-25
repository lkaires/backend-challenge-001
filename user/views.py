from django.shortcuts import render
from rest_framework import viewsets
from accounts.models import User
from user.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer