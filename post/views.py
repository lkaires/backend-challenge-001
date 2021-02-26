from django.shortcuts import render
from helpers.views import AuthorPermissionViewSet
from post.serializers import PostSerializer
from post.models import Post
from topic.models import Topic
from rest_framework.generics import get_object_or_404

class PostViewSet(AuthorPermissionViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # Returns topic pk (url_name)
    def get_topic(self):
        return get_object_or_404(Topic, url_name=self.kwargs.get('topic_url_name'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, topic=self.get_topic())

    def get_queryset(self):
        return Post.objects.filter(topic=self.get_topic())