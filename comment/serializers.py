from rest_framework import serializers
from comment.models import Comment
from post.models import Post

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    post = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'post', 'title', 'description', 'author', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at']


class NestedCommentSerializer(serializers.ModelSerializer):
    topic = serializers.SerializerMethodField()
    post = serializers.StringRelatedField()

    def get_topic(self, instance):
        return str(instance.post.topic)

    class Meta:
        model = Comment
        fields = ['id', 'topic', 'post', 'title']