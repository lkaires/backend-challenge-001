"""
API V1: Reddit Views
"""
###
# Libraries
###
from rest_framework import permissions, viewsets
from helpers.permissions import IsAuthorOrReadyOnly

from reddit.models import (
    Topic,
    Post,
    Comment,
)
from reddit.api.v1.serializers import (
    TopicSerializer,
    PostSerializer,
    CommentSerializer,
)


###
# Filters
###


###
# Viewsets
###

# For the challenge, each view should be on a respective app

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    lookup_field= 'url_name'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadyOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadyOnly]

    def get_queryset(self):
        return Post.objects.filter(topic__url_name=self.kwargs['topic_url_name'])

    def perform_create(self, serializer):
        author = self.request.user
        topic = Topic.objects.get(url_name=self.kwargs['topic_url_name'])
        serializer.save(author=author, topic=topic)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadyOnly]

    def get_queryset(self):
        return Comment.objects.filter(post__id=self.kwargs['post_pk'])

    def perform_create(self, serializer):
        author = self.request.user
        post = Post.objects.get(id=self.kwargs['post_pk'])
        serializer.save(author=author, post=post)