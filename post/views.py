from rest_framework import viewsets, permissions
from helpers.permissions import IsAuthorOrReadyOnly
from post.serializers import PostSerializer
from post.models import Post
from topic.models import Topic

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadyOnly]

    def get_queryset(self):
        return Post.objects.filter(topic__url_name=self.kwargs['topic_url_name'])

    def perform_create(self, serializer):
        author = self.request.user
        topic = Topic.objects.get(url_name=self.kwargs['topic_url_name'])
        serializer.save(author=author, topic=topic)