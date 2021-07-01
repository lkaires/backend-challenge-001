import topic
from rest_framework import serializers
from post.models import Post
from comment.serializers import CommentSerializer
from topic.models import Topic

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    created_at = serializers.DateTimeField(read_only=True)
    comment_count = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    topic = serializers.StringRelatedField()

    def get_comment_count(self, instance):
        # Returns number of comments on post
        return instance.comment.count()

    def get_comments(self, instance):
        # Returns 3 most recent comments on post
        return CommentSerializer(instance.comment, many=True, read_only=True, allow_null=True).data[:3]

    class Meta:
        model = Post
        fields = ['id', 'topic', 'title', 'description', 'author', 'created_at', 'updated_at', 'comment_count', 'comments']
        read_only_fields = ['id', 'created_at', 'comment_count', 'comments']
        fields = ['title', 'description', 'author', 'topic']


class NestedPostSerializer(serializers.ModelSerializer):
    topic = serializers.StringRelatedField()
    author = serializers.StringRelatedField()
    comment_count = serializers.SerializerMethodField()

    def get_comment_count(self, instance):
        return instance.comment.count()

    class Meta:
        model = Post
        fields = ['id', 'topic', 'title', 'author', 'created_at', 'updated_at', 'comment_count']