from rest_framework import serializers
from topic.models import Topic
from post.serializers import PostSerializer

class TopicSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    created_at = serializers.DateTimeField(read_only=True)
    posts = PostSerializer(many=True, allow_null=True, read_only=True)

    class Meta:
        model = Topic
        fields = ['url', 'url_name', 'title', 'description', 'author', 'created_at', 'updated_at', 'posts']