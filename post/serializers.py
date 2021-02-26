from rest_framework import serializers
from post.models import Post
from comment.serializers import CommentSerializer
from comment.models import Comment
from rest_framework.fields import SerializerMethodField

class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    topic = serializers.ReadOnlyField(source='topic.url_name')
    created_at = serializers.DateTimeField(read_only=True)
    comments = SerializerMethodField()

    def get_comments(self, instance):
        """
            Returns the 3 most recent comments
            Intended for list view
        """
        comments = Comment.objects.filter(post=instance.id)
        return CommentSerializer(comments, many=True, read_only=True, allow_null=True).data[3:]

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'description', 'created_at', 'updated_at', 'topic', 'comments']

class DetailPostSerializer(PostSerializer):
    def get_comments(self, instance):
        """
            Returns all comments
            Intended for detail view
        """
        comments = Comment.objects.filter(post=instance.id)
        return CommentSerializer(comments, many=True, read_only=True, allow_null=True).data