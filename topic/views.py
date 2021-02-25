from django.shortcuts import render
from helpers.views import AuthorPermissionViewSet
from topic.serializers import TopicSerializer
from topic.models import Topic

class TopicViewSet(AuthorPermissionViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)