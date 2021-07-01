from rest_framework import serializers
from topic.models import Topic
from post.serializers import NestedPostSerializer

class TopicSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    created_at = serializers.DateTimeField(read_only=True)
    post_count = serializers.SerializerMethodField()
    posts = serializers.SerializerMethodField()

    def get_post_count(self, instance):
        # Returns number of posts on topic
        return instance.posts.count()

    def get_posts(self, instance):
        # Returns 3 most recent posts on topic
        return NestedPostSerializer(instance.posts, many=True, allow_null=True).data[:3]

    class Meta:
        model = Topic
        fields = ['url_name', 'title', 'description', 'author', 'created_at', 'updated_at', 'post_count', 'posts']
        read_only_fields = ['url_name', 'created_at', 'post_count', 'posts']


class NestedTopicSerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()

    def get_post_count(self, instance):
        return instance.posts.count()

    class Meta:
        model = Topic
        fields = ['url_name', 'title', 'post_count']