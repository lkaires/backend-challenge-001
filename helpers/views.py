from rest_framework import permissions
from rest_framework import viewsets
from helpers.permissions import IsAuthorOrReadyOnly

class AuthorPermissionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadyOnly]