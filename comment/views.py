from django.shortcuts import render
from helpers.views import AuthorPermissionViewSet
from comment.serializers import CommentSerializer
from comment.models import Comment
from post.models import Post
from rest_framework.generics import get_object_or_404

class CommentViewSet(AuthorPermissionViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user,post=self.get_post())

    def get_queryset(self):
        return Comment.ordering.filter(post=self.get_post())