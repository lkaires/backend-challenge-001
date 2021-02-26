from rest_framework import serializers
from post.models import Post
from comment.serializers import CommentSerializer

class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    topic = serializers.ReadOnlyField(source='topic.title')
    created_at = serializers.DateTimeField(read_only=True)
    comments = CommentSerializer(many=True, allow_null=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'description', 'created_at', 'updated_at', 'topic', 'comments']