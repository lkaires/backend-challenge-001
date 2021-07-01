from rest_framework import permissions, viewsets
from helpers.permissions import IsAuthorOrReadyOnly

from topic.models import Topic
from topic.serializers import TopicSerializer

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    lookup_field= 'url_name'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadyOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)