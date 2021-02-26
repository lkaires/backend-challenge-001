from django.shortcuts import render
from helpers.views import AuthorPermissionViewSet, DetailViewSet
from topic.serializers import TopicSerializer, DetailTopicSerializer
from topic.models import Topic

class TopicViewSet(AuthorPermissionViewSet, DetailViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    detail_serializer_class = DetailTopicSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
