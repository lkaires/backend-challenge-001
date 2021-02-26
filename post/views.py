from django.shortcuts import render
from helpers.views import AuthorPermissionViewSet, DetailViewSet
from post.serializers import PostSerializer, DetailPostSerializer
from post.models import Post
from topic.models import Topic
from rest_framework.generics import get_object_or_404

class PostViewSet(AuthorPermissionViewSet, DetailViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    detail_serializer_class = DetailPostSerializer

    # Returns topic pk (url_name)
    def get_topic(self):
        return get_object_or_404(Topic, url_name=self.kwargs.get('topic_pk'))

    def get_queryset(self):
        return Post.objects.filter(topic=self.get_topic())

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, topic=self.get_topic())
