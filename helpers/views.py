from rest_framework import permissions
from rest_framework import viewsets
from helpers.permissions import IsAuthorOrReadyOnly

class AuthorPermissionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadyOnly]

class DetailViewSet(viewsets.ModelViewSet):
    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class

        return super(DetailViewSet, self).get_serializer_class()