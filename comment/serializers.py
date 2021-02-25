from rest_framework import serializers
from comment.models import Comment

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.ReadOnlyField(source='post.title')
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Comment
        fields = ['title', 'author', 'description', 'post', 'created_at', 'updated_at']