from rest_framework import permissions
from rest_framework import viewsets
from helpers.permissions import IsAuthorOrReadyOnly

class AuthorPermissionViewSet(viewsets.ModelViewSet):
    """
        Adds author permission to viewsets
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadyOnly]

class DetailViewSet(viewsets.ModelViewSet):
    """
        Sets different serializer to detail
        Intended to show different info in list and detail views
    """
    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class

        return super(DetailViewSet, self).get_serializer_class()