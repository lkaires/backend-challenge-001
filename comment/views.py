from rest_framework import viewsets, permissions
from helpers.permissions import IsAuthorOrReadyOnly
from comment.serializers import CommentSerializer
from comment.models import Comment
from post.models import Post

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadyOnly]

    def perform_create(self, serializer):
        author = self.request.user
        post = Post.objects.get(id=self.kwargs['post_pk'])
        serializer.save(author=author, post=post)

    def get_queryset(self):
        return Comment.objects.filter(post__id=self.kwargs['post_pk'])